> source: [https://crackmes.one/crackme/60db74bb33c5d410b88430dc](https://crackmes.one/crackme/60db74bb33c5d410b88430dc)

# Files

Input:
- [grandfather_clock](grandfather_clock) - Binary to crack

Output:
- [decode_pass.py](https://github.com/marciomat/reverse_engineering/tree/main/crackmesone/grandfatherClock/decode_pass.py) - Python script to decrypt the password
- [disassembly.md](https://github.com/marciomat/reverse_engineering/tree/main/crackmesone/grandfatherClock/disassembly.md) - Full disassembly of the `main()` function (with renamed local variables for clarity)

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

We list all functions and we see `main()` accessible. Looking into the `main()` we can right away identify how it accesses the argument passed via the command line:

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
> - And if there are more arguments, they're pushed into the stack

## Validating the user input

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
We know that the command line parameters in C are always passed via a _vector[ ]_ and each position of the _vector[ ]_ contains the string to a parameter.

We also know that the first parameter is always the file _path/name_. And we're not interested in that.
We want to access the second position of the `argv_in[]` vector. That's why in the second line of the code block above it is adding 8 to the pointer.

To see this in practice, I printed the first and second position of the `argv_in`. Notice how to print the second position, by simply adding 8:

```
:> pf S @ rax
0x7ffc856ad8c8 = 0x7ffc856ad8c8 -> 0x7ffc856ae2a0 "/home/<user>/re/crackmesone/grandfatherClock/grandfather_clock"
:> pf S @ rax + 8
0x7ffc856ad8d0 = 0x7ffc856ad8d0 -> 0x7ffc856ae2df "my_flag"
```

Moving on, after accessing the input passed by the user, it calls `strlen()` and with the result it does a bit-logic `AND` with `0x1`, followed by a check if `rax` is zero.
This means that the software is checking if the number of _chars_ in the input string is _even_ (as opposed to _odd_).

If the number of _chars_ is _odd_ it terminates the execution.

> The reason for this check will become more apparent later on.

## The misterious function

If the number of _chars_ is _even_, it continues the execution:

```assembly
│      │└─> 0x55629d85043a      488b45f0       mov rax, qword [argv_in]
│      │    0x55629d85043e      4883c008       add rax, 8              ; again, skip the 1st argv
│      │    0x55629d850442      488b00         mov rax, qword [rax]
│      │    0x55629d850445      4889c7         mov rdi, rax
│      │    0x55629d850448      e8d4feffff     call sym._99adb5ad_c9d1_44ff_84ce_b52782ac7aeb
│      │    0x55629d85044d      4889c6         mov rsi, rax
```

Here it accesses again the second parameter from the command line (i.e. the input provided by the user) and passes it as argument to a misterious function.

In situations like this we always have a decision to make:

- Do we dive in the function to understand its inner workings?

- Or do we use a debugger, let the function run its magic (as a black-box) and we hopefully get to understand what it does after trying different inputs?

In this case I opted for the latter. And luckily it was quite straighforward to understand what this magic function is doing.

<br/>

I used as input: `abcd`

And I got as output:

```
:> ps @ rax
DBAC
```

So first it made each _char_ into upper-case. This is accomplished by subtracting `0x20` from the ASCII char.

But what happens if the input is already upper-case? It still subtracts `0x20`! So for ex, if the input is `AB` (ASCII code: 0x41 and 0x42), the output would be `!"` (ASCII code: 0x21 and 0x22).

The second thing that the misterious function did was to scramble the letters in a pattern that seems to oscilate like a pendulum (and that's why the name of this challenge!).

> And now we know why the number of _chars_ in the user input has to be _even_.
>
> It's because the pattern for this scramble uses pairs of _chars_ to put them in opposite extremes of the output string

## The encoded flag!

In the following step, it calls `strlen()` passing 2 arguments:

- Arg1 (`rdi`): data store in the address `0x55be44f3b020`
- Arg2 (`rsi`): our scrambled user input


```assembly
│           0x55be44f3a44d      4889c6         mov rsi, rax                                                                                                                                                                                      
│           0x55be44f3a450      488d05c90b00.  lea rax, obj._867a0be1_691e_4546_9b6c_020df3bcdc93 ; 0x55be44f3b020 ; "]\x10\x14LC\x10CNM\x14?GL4#&A[(R\x10\x11?S\x11LTR"                                                                         
│           0x55be44f3a457      4889c7         mov rdi, rax
│           0x55be44f3a45a      e831fcffff     call sym.imp.strcmp
│           0x55be44f3a45f      85c0           test eax, eax
│       ┌─< 0x55be44f3a461      7416           je 0x55be44f3a479
```

It's very clear that whatever data is stored in the hardcoded address is our scrambled flag.

Let's take a look into that:

```
:> px 30 @ rax
- offset -       0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x55be44f3b020  5d10 144c 4310 434e 4d14 3f47 4c34 2326  ]..LC.CNM.?GL4#&
0x55be44f3b030  415b 2852 1011 3f53 114c 5452 0000       A[(R..?S.LTR..
```

The first thing to look for is the `NULL` char (i.e. `0x00`) since `strcmp()` uses it to know where the strings end.

Based on that we can guess how many letters our flag has.

Also we can do a quick sanity check and confirm that all bytes are bigger or equal to `0x01` and smaller or equal to `0x5D`.

We know that since all _chars_ have to be a printable _char_. And by looking at the ASCII table we can see that printable _chars_ range from `0x21` (as `!`) to `0x7D` (as `}`). But the scrambling function was subtracting `0x20` from every _char_.

And that sequence of bytes indeed are all in this interval, which is good news!

## Using a script to decode our flag

Now we have all the information we need to be able to decode our flag.

We know what is our encoded flag and we know how to unscramble it.

I created this quick [python script](https://github.com/marciomat/reverse_engineering/tree/main/crackmesone/grandfatherClock/decode_pass.py) which is quite easy to understand and _voila_! It worked!
