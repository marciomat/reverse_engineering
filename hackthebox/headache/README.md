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
As we can see, this jump is skipping the `call main` and, instead, it calls `fcn.000013c1`.

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

And of course this `fcn.000013c1` looks just like a `main()` function. Meaning, it executes the same instructions to print the same messages we see on the screen when we run the binary.

And there is, in fact, a flag hidden there! But it's a fake flag...

The easiest way to proceed here is to edit the binary and change the `jne 0x1352` instruction.
There are many options here. We can simply swap from `jne` to `je` or replace the `jne` with 2 `nop`.

I used the latter approach and saved the new binary as `patched_headache`. This is the binary I'll be using from here on.

## Real main() function, but encrypted!

