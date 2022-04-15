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

Just to prove it, we can maually decode the data. For example, in the table below we have the first 2 bytes from the encoded `main()`, followed by the hardcoded string and finally the decoded `main()`.

| encoded `main()` | hardcoded string | decoded `main()` |
| ---------------- | ---------------- | ---------------- |
| `0x34` | `0x61` | `0x34 xor 0x61 == 0x55` |
| `0x79` | `0x31` | `0x79 xor 0x31 == 0x48` |

If you look back at the `main()` function, these are exactly the bytes found at the beginning of the function.

But most importantly, it always decode `main()` function the same way, whether a debugger is being used or not.
So there is not much to fight with this decoder. We just execute the binary and let it work its magic before we analyze the instructions from `main()`.

## Close, but no cigar

We made a lot of progress so far!
Let's examine the real `main()` function after it gets decoded.

Few lines down the road we can see the following instructions:

```assembly
            0x55e05d0c6089      c645a048       mov byte [rbp - 0x60], 0x48    ; 'H' ; 72
            0x55e05d0c608d      c645a154       mov byte [rbp - 0x5f], 0x54    ; 'T' ; 84
            0x55e05d0c6091      c645a242       mov byte [rbp - 0x5e], 0x42    ; 'B' ; 66
            0x55e05d0c6095      c645a37b       mov byte [rbp - 0x5d], 0x7b    ; '{' ; 123
            0x55e05d0c6099      c645a477       mov byte [rbp - 0x5c], 0x77    ; 'w' ; 119
            0x55e05d0c609d      c645a530       mov byte [rbp - 0x5b], 0x30    ; '0' ; 48
            0x55e05d0c60a1      c645a677       mov byte [rbp - 0x5a], 0x77    ; 'w' ; 119
            0x55e05d0c60a5      c645a75f       mov byte [rbp - 0x59], 0x5f    ; '_' ; 95
            0x55e05d0c60a9      c645a874       mov byte [rbp - 0x58], 0x74    ; 't' ; 116
            0x55e05d0c60ad      c645a968       mov byte [rbp - 0x57], 0x68    ; 'h' ; 104
            0x55e05d0c60b1      c645aa34       mov byte [rbp - 0x56], 0x34    ; '4' ; 52
            0x55e05d0c60bd      c645ad5f       mov byte [rbp - 0x53], 0x5f    ; '_' ; 95
            0x55e05d0c60c1      c645ae63       mov byte [rbp - 0x52], 0x63    ; 'c' ; 99
            0x55e05d0c60c5      c645af30       mov byte [rbp - 0x51], 0x30    ; '0' ; 48
            0x55e05d0c60c9      c645b030       mov byte [rbp - 0x50], 0x30    ; '0' ; 48
            0x55e05d0c60cd      c645b130       mov byte [rbp - 0x4f], 0x30    ; '0' ; 48
            0x55e05d0c60d1      c645b26c       mov byte [rbp - 0x4e], 0x6c    ; 'l' ; 108
            0x55e05d0c60d5      c645b37d       mov byte [rbp - 0x4d], 0x7d    ; '}' ; 125
            0x55e05d0c60d9      488d45c0       lea rax, [rbp - 0x40]
            0x55e05d0c60dd      4889c7         mov rdi, rax
            0x55e05d0c60e0      e87befffff     call sym.imp.strlen
            0x55e05d0c60e5      4883f814       cmp rax, 0x14           ; 20
```

Looks like the flag! But... of course it's a fake flag. We are still not out of the woods.

But, notice the last instruction, comparing the `strlen` with `0x14`. The length of the flag is probably 20 characters.

## How many more traps?

Clearly there is another call to `ptrace` somewhere else. And this is causing the debugger to execute a different code compared to when we just run the binary from the command-line.

Like I mentioned before, part of the instructions are still obfuscated, so I can't see the `ptrace` call. But even if I could see it, I wouldn't be able to easily patch it, because `main()` is encoded.
It wouldn't be impossible to patch since we know how the decoding algorithm works. But let's take an easier approach.

---

We know which messages it prints on the screen, so we can find their address and search for the references.

Let's look at the references to "Login success!":

```
:> axt @ 0x562ccf3f5056
fcn.000013c1 0x562ccf3f352c [DATA] lea rdi, [0x562ccf3f5056]
(nofunc) 0x562ccf3f41b5 [DATA] lea rdi, [0x562ccf3f5056]
(nofunc) 0x562ccf3f466e [DATA] lea rdi, [0x562ccf3f5056]
```

The first appearance is from the fake `main()` function that we are bypassing already.

The last 2 are from the real `main()` function. The first one is for the fake flag, so the second one should be for the real flag?

## The final countdown

By looking at the address of the third reference to "Login success!" we can assume there are more useful code towards the end of the `main()` function, that normally don't get executed when a debugger is in use.

Scrolling down we see this:

```assembly
            0x562ccf3f4214      c68541ffffff.  mov byte [rbp - 0xbf], 0xfe    ; 254
            0x562ccf3f421b      c68542ffffff.  mov byte [rbp - 0xbe], 0x8d    ; 141
            0x562ccf3f4222      c68543ffffff.  mov byte [rbp - 0xbd], 0xd    ; 13
            0x562ccf3f4229      c68544ffffff.  mov byte [rbp - 0xbc], 0xd2    ; 210
            0x562ccf3f4230      c68545ffffff.  mov byte [rbp - 0xbb], 0xe4    ; 228
            0x562ccf3f4237      c68546ffffff.  mov byte [rbp - 0xba], 0xfe    ; 254
            0x562ccf3f423e      c68547ffffff.  mov byte [rbp - 0xb9], 8
            0x562ccf3f4245      c68548ffffff.  mov byte [rbp - 0xb8], 0xef    ; 239
            0x562ccf3f424c      c68549ffffff.  mov byte [rbp - 0xb7], 0x57    ; 'W' ; 87
            0x562ccf3f4253      c6854affffff.  mov byte [rbp - 0xb6], 0x47    ; 'G' ; 71
            0x562ccf3f425a      c6854bffffff.  mov byte [rbp - 0xb5], 0xdb    ; 219
            0x562ccf3f4261      c6854cffffff.  mov byte [rbp - 0xb4], 0x4d    ; 'M' ; 77
            0x562ccf3f4268      c6854dffffff.  mov byte [rbp - 0xb3], 0x96    ; 150
            0x562ccf3f426f      c6854effffff.  mov byte [rbp - 0xb2], 0x2f    ; '/' ; 47
            0x562ccf3f4276      c6854fffffff.  mov byte [rbp - 0xb1], 0x3b    ; ';' ; 59
            0x562ccf3f427d      c68550ffffff.  mov byte [rbp - 0xb0], 0xa8    ; 168
            0x562ccf3f4284      c68551ffffff.  mov byte [rbp - 0xaf], 0xbb    ; 187
            0x562ccf3f428b      c68552ffffff.  mov byte [rbp - 0xae], 0x70    ; 'p' ; 112
            0x562ccf3f4292      c68553ffffff.  mov byte [rbp - 0xad], 0x11    ; 17
            0x562ccf3f4299      c68554ffffff.  mov byte [rbp - 0xac], 0xad    ; 173
            0x562ccf3f42a0  ~   c745f8000000.  mov dword [rbp - 8], 0
```

Which really looks like the initialization of a flag. Just like the fake flag initialization.

But this one seems to be encrypted, so it makes me believe this should be the one.

Using the following command we can jump to the beginning of the code above:

```
:> dr rip=0x562ccf3f4214
0x562ccf3f334b ->0x562ccf3f4214
```

We continue the execution until we run into the references to "Login success!" and "Login Failed!".

```assembly
        ╎   0x562ccf3f4628      c1e002         shl eax, 2
        ╎   0x562ccf3f462b      09d0           or eax, edx
        ╎   0x562ccf3f462d      8845e7         mov byte [rbp - 0x19], al
        ╎   0x562ccf3f4630      806de746       sub byte [rbp - 0x19], 0x46    ; [0x46:1]=255 ; 70
        ╎   0x562ccf3f4634      f65de7         neg byte [rbp - 0x19]
        ╎   0x562ccf3f4637      0fb655e7       movzx edx, byte [rbp - 0x19]
        ╎   0x562ccf3f463b      8b45f8         mov eax, dword [rbp - 8]
        ╎   0x562ccf3f463e      0fb64405c0     movzx eax, byte [rbp + rax - 0x40]
        ╎   0x562ccf3f4643      0fbec0         movsx eax, al
        ╎   0x562ccf3f4646      39c2           cmp edx, eax
       ┌──< 0x562ccf3f4648      7416           je 0x562ccf3f4660
       │╎   0x562ccf3f464a  ~   488d3df70900.  lea rdi, [0x562ccf3f5048]    ; "Login Failed!"
```

Here we can see the instruction `cmp edx, eax` followed by a conditional jump.
This jump skips the instruction that loads "Login Failed!".

A breakpoint in the `cmp edx, eax` reveals that `eax` holds the first character of the string that we used as input.
Which probably means that `edx` is holding the flag!

It's comparing one character at a time, and if any of the checks fail, it stops the loop and prints "Login Failed!".
So we need to temporarily patch the conditional jump so we can loop over every char.

We can use the following instruction for that:

```
wao jne
```

This converts the `je` to `jne`.

Now we just need to loop over 20 times and take note of the real flag!

The final test:

```
$ ./headache 
Initialising.....
Enter the key: HTB{l4yl3_w4s_h3r3!}
Login success!
```