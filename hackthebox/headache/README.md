> source: [https://app.hackthebox.com/challenges/headache](https://app.hackthebox.com/challenges/headache)

# Files

Input:
- [headache](headache) - Original binary to crack

Output:
- [patched_headache](patched_headache) - Patched version to help debug, bypassing checks

# The challenge

From the outside it looks just like any other CTF challenge:

```
$ ./headache                           
Initialising.....
Enter the key: abcde
Login Failed!
```

But on the inside this challenge is a beast!

# Solution

This binary uses 2 main tricks to hide the flag:

- It uses `ptrace` calls (in more than one place) to check if a debugger is being used to change its behavior.
- And it also modifies itself at runtime. The `main()` function is decrypted right before being called.

> For more information on how `ptrace` is used to detect a debugger, check my write-up for [bombsLanded](../bombsLanded#debugger-protection)

## Fake main() function

The tricks start even before `main()` function call.

Here we can see, in the third line, a jump instruction `jne 0x1352` right after a `cmp dword [rbp - 4], 0`.
As we can see, this jump is skipping the call to `main` and, instead, it calls `fcn.000013c1`.

```assembly
            0x0000130b      488d3df61c00.  lea rdi, [0x00003008]       ; "a15abe90c112d09369d9f9da9a8c046e"
            0x00001312      e8bb0b0000     call fcn.00001ed2           ;[3]
            0x00001317      837dfc00       cmp dword [rbp - 4], 0
        ┌─< 0x0000131b      7535           jne 0x1352
        │   0x0000131d      488b052c3e00.  mov rax, qword [obj.stdout]    ; [0x5150:8]=0
        │   0x00001324      4889c7         mov rdi, rax
        │   0x00001327      e8a4fdffff     call sym.imp.fflush         ;[4] ; int fflush(FILE *stream)
        │   0x0000132c      488d35511300.  lea rsi, [0x00002684]
        │   0x00001333      488d3d750c00.  lea rdi, [main]
        │   0x0000133a      e8f40a0000     call fcn.00001e33           ;[5]
        │   0x0000133f      488b55f0       mov rdx, qword [rbp - 0x10]
        │   0x00001343      8b45fc         mov eax, dword [rbp - 4]
        │   0x00001346      4889d6         mov rsi, rdx
        │   0x00001349      89c7           mov edi, eax
        │   0x0000134b      e85f0c0000     call main                   ;[6] ; int main(uint32_t argc, char **argv, int64_t arg4)
       ┌──< 0x00001350      eb0b           jmp 0x135d
       ││   ; CODE XREF from str.YzI @ +0x32
       │└─> 0x00001352      b800000000     mov eax, 0
       │    0x00001357      e865000000     call fcn.000013c1           ;[7]
       │    0x0000135c      90             nop
       │    ; CODE XREF from str.YzI @ +0x67
       └──> 0x0000135d      c9             leave
            0x0000135e      c3             ret
```

And of course this `fcn.000013c1` looks just like a `main()` function. Meaning, it executes the instructions to print the same messages we see on the screen when we run the binary.

And there is, in fact, a flag hidden there! But it's a fake flag...

The easiest way to make sure we can debug the real `main()` function is to edit the binary and change the `jne 0x1352` instruction.
There are many options here. We can simply swap from `jne` to `je` or replace the `jne` with 2 `nop`.

I used the latter approach and saved the new binary as `patched_headache`. This is the binary I'll be using from here on.

## Real main() function, but encrypted!

With the patched binary we can access the real `main()` function while debugging it.

But when we look at it, this is what we see:

```assembly
 53: int main (uint32_t argc, char **argv, int64_t arg4);
│       ╎   ; arg uint32_t argc @ rdi
│       ╎   ; arg char **argv @ rsi
│       ╎   ; arg int64_t arg4 @ rcx
│      ┌──> 0x00001faf      3479           xor al, 0x79
│      ╎╎   0x00001fb1      bc842ae4d5     mov esp, 0xd5e42a84
│     ┌───< 0x00001fb6      e063           loopne 0x201b
│     │╎╎   0x00001fb8      3131           xor dword [rcx], esi        ; arg4
│     │╎╎   0x00001fba      bbd90cc6cc     mov ebx, 0xccc60cd9
│     │╎╎   0x00001fbf      c9             leave
│     │└──< 0x00001fc0      71ed           jno main
```

These instructions seem very random and don't make sense. 

And when we look at the rest of the function, we can't see any instruction to print the messages we expect to see on the screen.
So there is something else going on.

If we run the binary and set a breakpoint right before we enter `main()`, this is what we see:

```assembly
┌ 53: int main (int argc, char **argv, char **envp);
│           ; arg uint32_t argc @ rdi
│           ; arg char **argv @ rsi
│           ; arg int64_t arg4 @ rcx
│           0x55e05d0c5faf      55             push rbp
│           0x55e05d0c5fb0      4889e5         mov rbp, rsp
│           0x55e05d0c5fb3  ~   4881ecd00000.  sub rsp, 0xd0
│           0x55e05d0c5fb8      0000           add byte [rax], al      ; arg4
│           0x55e05d0c5fba      89bd3cffffff   mov dword [rbp - 0xc4], edi
│           0x55e05d0c5fc0  ~   4889b530ffff.  mov qword [rbp - 0xd0], rsi
│           0x55e05d0c5fc2      b530           mov ch, 0x30            ; '0' ; 48 ; argv
```

The instructions changed. It looks like they're re-written at runtime.

And now when analyzing the rest of the function, the instructions make more sense.

> Note: There are still many weird instructions being shown by radare2. I'm not exactly sure what is going on, but it may be another obfuscation technique used by the binary. I don't know how to completely fix it but we can still see enough of the code to work with it.

## The transformation of main()

By analyzing the code and running some experiments we can quickly find the function responsible for decoding `main()`.
The function is `fcn.00001e33`. And it's called right before `main()`:

```assembly
            0x55e05d0c5324      4889c7         mov rdi, rax
            0x55e05d0c5327      e8a4fdffff     call sym.imp.fflush     ;[3] ; int fflush(FILE *stream)
            0x55e05d0c532c      488d35511300.  lea rsi, [0x55e05d0c6684]
            0x55e05d0c5333      488d3d750c00.  lea rdi, [main]         ; 0x55e05d0c5faf
            0x55e05d0c533a      e8f40a0000     call fcn.00001e33       ;[4]
            0x55e05d0c533f      488b55f0       mov rdx, qword [rbp - 0x10]
            0x55e05d0c5343      8b45fc         mov eax, dword [rbp - 4]
            0x55e05d0c5346      4889d6         mov rsi, rdx
            0x55e05d0c5349      89c7           mov edi, eax
            0x55e05d0c534b      e85f0c0000     call main
```

We can take a deep look into this function but at the end of the day, it does exactly what we expect. It decodes the data from `main()`.

It uses a string of hardcoded bytes and perform a `xor` operation between these bytes and the hex data that is already in the `main()`.
The hardcoded bytes are:

```
:> px 32 @ 0x55e05d0c7008
- offset -       0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x55e05d0c7008  6131 3561 6265 3930 6331 3132 6430 3933  a15abe90c112d093
0x55e05d0c7018  3639 6439 6639 6461 3961 3863 3034 3665  69d9f9da9a8c046e
```

We can maually decode the data. For example in the table below we have the bytes from the encoded `main()`,the hardcoded string used to decode and the decoded `main()`.

| encoded `main()` | hardcoded string | decoded `main()` |
| ---------------- | ---------------- | ---------------- |
| `0x34` | `0x61` | `0x34 xor 0x61 == 0x55` |
| `0x79` | `0x31` | `0x79 xor 0x31 == 0x48` |


But most importantly, it always decode `main()` function the same way, whether a debugger is being used or not.
So there is not much to fight with this decoder. We just execute the binary and let it work its magic before we analyze the instructions from `main()`.

## More fake flags

