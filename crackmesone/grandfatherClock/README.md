> source: https://crackmes.one/crackme/60db74bb33c5d410b88430dc

# Tools used

- radare2

# Files

Input:
- [grandfather_clock](grandfather_clock) - Binary to crack

Output:
- [decode_pass.py](decode_pass.py) - Python script to decrypt the password
- [disassembly.md](disassembly.md) - Full disassembly of the `main()` function (with renamed local variables for clarity)

# The challenge

This is a classic CrackMe with an encoded password inside the binary. The password is the flag for the challenge.

> And an interesting difference in this challenge is that the flag is passed via argument in the command line.
So in the analysis of the binary we will be able to see how the access to the argument is handled in assembly.

```
$ ./grandfather_clock my_flag
That's not the flag!
```

# Solution

First we open the binary in _radare2_ and analyze it:

```
$ r2 -A grandfather_clock
```

We list all functions and we see `main()` accessible. Looking into the `main()` we can right away identify how it handles the argument passed via the command line:

```assembly
│           0x55f8eb1c43e3      897dfc         mov dword [var_4h], edi    ; argc
│           0x55f8eb1c43e6      488975f0       mov qword [argv_in], rsi    ; argv
```

So clearly the vector of arguments is stored in the local variable `argv_in` (renamed by me for clarity).

> In order to understand better those 2 lines of assembly, it's important to remember the [_calling convention_](https://en.wikipedia.org/wiki/X86_calling_conventions) for x86.
>
> In this case the convetion specifies that the arguments are passed in the following order:
> - RDI (Note: EDI is the lower 32-bits of RDI)
> - RSI
> - RDX
> - RCX
> - R8
> - R9
> - And if there are more arguments, they're _pushed_ into the stack

---

Next, we have the following check:

```assembly
│      │└─> 0x55f8eb1c4409      488b45f0       mov rax, qword [argv_in]
│      │    0x55f8eb1c440d      4883c008       add rax, 8       ; skip 1st argv (i.e. file path/name) 
│      │    0x55f8eb1c4411      488b00         mov rax, qword [rax]
│      │    0x55f8eb1c4414      4889c7         mov rdi, rax
│      │    0x55f8eb1c4417      e844fcffff     call sym.imp.strlen
│      │    0x55f8eb1c441c      83e001         and eax, 1
│      │    0x55f8eb1c441f      4885c0         test rax, rax
│      │┌─< 0x55f8eb1c4422      7416           je 0x55f8eb1c443a
```

The first interesting thing to look at is how to get the parameter passed via command line.
We know that the command line parameters in C are always passed via a _vector[ ]_ and each position of the _vector[ ]_ contains the string to the parameter.

We also know that the first parameter is always the file _path/name_. And we're not interested in that.
We want to access the second position of the `argv_in[]` vector. That's why in the second line of the code block above it is adding 8 to the pointer to the vector.

To see this in practice, I printed the first and second position of the `argv_in`. Notice how to print the second position, by simply adding 8:

```
:> pf S @ rax
0x7ffc856ad8c8 = 0x7ffc856ad8c8 -> 0x7ffc856ae2a0 "/home/<user>/re/crackmesone/grandfatherClock/grandfather_clock"
:> pf S @ rax + 8
0x7ffc856ad8d0 = 0x7ffc856ad8d0 -> 0x7ffc856ae2df "abcd"
```

Moving on, after accessing the _input_ passed by the user, it calls `strlen()` and does a bit-logic `AND` with `0x1`, followed by a check if `rax` is zero.
This means that the software is checking if the number of _chars_ in the input string is _even_ (as opposed to _odd_).

If the number of _chars_ is _odd_ it terminates the execution.

> The reason for this check will become more apparent later on.

---

If the number of _chars_ is _even_, it continues execution:

```assembly
│      │└─> 0x55629d85043a      488b45f0       mov rax, qword [argv_in]
│      │    0x55629d85043e      4883c008       add rax, 8              ; again, skip the 1st argv
│      │    0x55629d850442      488b00         mov rax, qword [rax]
│      │    0x55629d850445      4889c7         mov rdi, rax
│      │    0x55629d850448      e8d4feffff     call sym._99adb5ad_c9d1_44ff_84ce_b52782ac7aeb
│      │    0x55629d85044d      4889c6         mov rsi, rax
```

Here it access again the second parameter from the command line (i.e. the input provided by the user) and passes it as argument to a misterious function.

In these situations we always have a decision to make.

- Do we dive in the function and understand its inner workings?

- Or do we use a debugger, let the function run its magic, as a black-box, and we hopefully get to understand what it does after trying different inputs?

In this case I opted for the latter. And luckily it was quite straighforward to understand what this magic function is doing.

<br/>

I used as input: `abcd`

And I got as output:

```
:> ps @ rax
DBAC
```

So first it made it all upper-case. This is accomplished by subtracting `0x20` from the ASCII char.

But what happens if the input is already upper-case? It still subtracts `0x20`! So for ex, if the input is `AB` (ASCII code: 0x41 and 0x42), the output would be `!"` (ASCII code: 0x21 and 0x22).
