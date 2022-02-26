> source: [https://play.picoctf.org/practice?page=1&search=checkpass](https://play.picoctf.org/practice?page=1&search=checkpass)

# Files

Input:
- [checkpass](checkpass) - Original binary to crack

Output:
- [hack_checkpass.py](hack_checkpass.py) - Python script used to crack the password
- [assembly.md](assembly.md) - Full disassembly of the main part of the code

# The challenge

This binary receives the password input via the first call parameter.
And we have to find the right password:

```
$ ./checkpass password_attempt
Invalid length
```

The first obvious thing to notice is the error message.
It gives us a first clue since it tells us that the legnth is invalid.

So if we feel like bruteforcing it we can try multiple different passwords until we find the right lenght.
But later on we will find the check in the code.

# Solution

This binary is stripped. We can still find the `main()` function but there is nothing interesting there.
And the entire code is quite well obfuscated (at least for my level of experience!).

For this reason I won't go into too many details on how I got to each detail since I myself was lost for so long.

> A very long disassembly of this entire analysis is available at [assembly.md](assembly.md).

## Initial checks

This is the first part of the code where the initial checks are executed:

```assembly
        │   0x564966c059c5      4883782829     cmp qword [rax + 0x28], 0x29    ; Compare password lenght with 41 (0x29)
       ┌──< 0x564966c059ca      0f8599000000   jne 0x564966c05a69
       ││   0x564966c059d0      488b5818       mov rbx, qword [rax + 0x18]
       ││   0x564966c059d4      488d059d4303.  lea rax, [0x564966c39d78]
       ││   0x564966c059db      4839c3         cmp rbx, rax
      ┌───< 0x564966c059de      7413           je 0x564966c059f3
      │││   0x564966c059e0      48b87069636f.  movabs rax, 0x7b4654436f636970  ; check if password starts with 'picoCTF{'
      │││   0x564966c059ea      483903         cmp qword [rbx], rax
     ┌────< 0x564966c059ed      0f85e0000000   jne 0x564966c05ad3
     ││││   ; CODE XREF from rip @ +0x19
     │└───> 0x564966c059f3      488d4328       lea rax, [rbx + 0x28]
     │ ││   0x564966c059f7      488d0d964303.  lea rcx, [0x564966c39d94]
     │ ││   0x564966c059fe      4839c8         cmp rax, rcx
     │┌───< 0x564966c05a01      7409           je 0x564966c05a0c
     ││││   0x564966c05a03      80387d         cmp byte [rax], 0x7d    ; compares last char with '}'
    ┌─────< 0x564966c05a06      0f85c7000000   jne 0x564966c05ad3
```

From my comments in the code above we can see where it checks for the password lenght (41) and also checks if the password starts with `picoCTF{` and ends with `}`.

So now we know how the password has to look like, and we also know that the actual password will have 32 characters (41 - `picoCTF{}`).

## Lost in assembly, saved by Ghidra

Here is the part where I got lost. The code that comes after this initial check seemed very confusing to me.

So I decided to look at the code through Ghidra to see what kind of C code it would generate.
I won't paste the entire code here but the most important part is this:

```c
          if (lStack176 == 0) {
            local_128 = (undefined **)*local_c0;
            uStack288 = local_c0[1];
            local_118 = local_c0[2];
            uStack272 = *(undefined4 *)(local_c0 + 3);
            uStack268 = *(undefined4 *)((long)local_c0 + 0x1c);
            lStack176 = lStack176 + 0x20;
            FUN_001054e0(local_70,&local_128,0);
            uStack272 = uStack88;
            uStack268 = uStack84;
            FUN_001054e0(local_50,&local_128,1);
            uStack272 = uStack56;
            uStack268 = uStack52;
            FUN_001054e0(&local_a8,&local_128,2);
            uStack272 = uStack144;
            uStack268 = uStack140;
            FUN_001054e0(&local_e0,&local_128,3);
            local_e9 = local_dd;
            local_e3 = local_dc;
            local_ec = local_db;
            local_e1 = local_da;
            local_f0 = local_d9;
            local_e7 = local_d8;
            local_e2 = local_d6;
            local_ee = local_d5;
            local_e5 = local_d3;
            local_f1 = local_d1;
            local_ed = local_d0;
            local_e6 = local_cf;
            local_e4 = local_ce;
            local_ea = local_cc;
            local_eb = local_cb;
            local_ef = local_ca;
            local_e8 = local_c4;
            local_f2 = local_c2;
            local_128 = (undefined **)0x19;
            local_f5 = local_de;
            if ((((((local_c7 == -0x1a) && (local_128 = (undefined **)0x0, local_e0 == '\x1f')) &&
                  (local_128 = (undefined **)0xe, local_d2 == -7)) &&
                 ((local_128 = (undefined **)0x13, local_cd == 't' &&
                  (local_128 = (undefined **)0x17, local_c9 == '\"')))) &&
                ((((local_128 = (undefined **)0x1, local_df == 'h' &&
                   ((local_128 = (undefined **)0x1d, local_c3 == -7 &&
                    (local_128 = (undefined **)0x1b, local_c5 == -0x39)))) &&
                  ((local_128 = (undefined **)0x1a, local_c6 == -0x73 &&
                   (((((local_128 = (undefined **)0xc, local_d4 == '\"' &&
                       (local_128 = (undefined **)0x1f, local_c1 == '{')) &&
                      (local_128 = (undefined **)0x6, local_da == ':')) &&
                     ((local_128 = (undefined **)0xa, local_d6 == -0x52 &&
                      (local_128 = (undefined **)0xf, local_d1 == 'H')))) &&
                    (local_128 = (undefined **)0x1e, local_c2 == '1')))))) &&
                 (((((local_128 = (undefined **)0x7, local_d9 == -0x35 &&
                     (local_128 = (undefined **)0xb, local_d5 == -0x35)) &&
                    ((local_128 = (undefined **)0x5, local_db == '\"' &&
                     (((local_128 = (undefined **)0x16, local_ca == 'F' &&
                       (local_128 = (undefined **)0x10, local_d0 == '\x05')) &&
                      (local_128 = (undefined **)0x15, local_cb == -0x32)))))) &&
                   ((local_128 = (undefined **)0x3, local_dd == '>' &&
                    (local_128 = (undefined **)0x14, local_cc == -0x33)))) &&
                  (local_128 = (undefined **)0x8, local_d8 == '+')))))) &&
               ((((local_128 = (undefined **)0x1c, local_c4 == '\x12' &&
                  (local_128 = (undefined **)0xd, local_d3 == ' ')) &&
                 ((local_128 = (undefined **)0x11, local_cf == '{' &&
                  (((local_128 = (undefined **)0x2, local_de == 'P' &&
                    (local_128 = (undefined **)0x9, local_d7 == -0x7d)) &&
                   (local_128 = (undefined **)0x4, local_dc == -0x48)))))) &&
                ((local_128 = (undefined **)0x18, local_c8 == -0x31 &&
                 (local_128 = (undefined **)0x12, local_ce == '{')))))) {
              FUN_001066a0();
            }
            else {
              FUN_00106650();
```

We can see the function `FUN_001054e0()` is called 4 times. And the second parameter is always the same `&local_128`, while the third parameter is a number incrementing from `0` to `3`.

The interesting part is that the first time this function is called, `local_128` contains the password we typed!
After returning from the first call, `local_128` will have a messy sequence of bytes.
And after that `FUN_001054e0()` is called 3 more times, to scramble even more our password.

I'm not a cryptography expert, so I can't recognize what this function is doing.
But by looking at the write-up for this challenge, it seems like this function performs a S-Box transformation.

Since it would take me way too long to understand this function I took another path.

But before moving forward, there are 2 more things to notice in the code above:

1. We have a long list of checks inside an `if` statement. And we have 32 lines of checks! Remeber that our password has 32 characeters?
2. If all checks in the `if` statement are true, it calls the function `FUN_001066a0()`. And not surprisingly, this function prints `Success`!

> Note: Remember when I said this code has some obfuscation? This is the code of the function that prints `Success`:
> ```c
> void FUN_001066a0(void)
> 
> {
>   undefined **local_30;
>   undefined8 local_28;
>   undefined8 local_20;
>   char *local_10;
>   undefined8 local_8;
>   
>   local_30 = &PTR_DAT_00348298;
>   local_28 = 1;
>   local_20 = 0;
>   local_10 = "Invalid password\n";
>   local_8 = 0;
>   FUN_001083b0(&local_30);
>   FUN_0011f1d0(0);
>   do {
>     invalidInstructionException();
>   } while( true );
> }
> ```
>
> Looks like it's printing `Invalid password`, right? Wrong!...

## Time for Python!

If my approach isn't by reverse-engineering `FUN_001054e0()`, I can try to brute-force.

This is a different brute-force technique (at least for me), since I can't easily replicate the contents of `FUN_001054e0()` inside my python script.
So I decided to try something new and use `r2pipe`, which is describe as `The simplest and most effective way to script radare2`.
It means I can execute the binary, and have access to all it's internal registers at runtime through radare2's debugger.

The main idea of the script is to first run the binary with a dummy password:
`picoCTF{ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ}`

It will fail at the very first check in the `if` statement we saw in the Ghidra code.
Since it looks like each line of the `if` statement is checking one character of the password, it means we can probably crack the password one character at a time!

The first problem: We don't know which character of the password each line is checking since it's all scrambled.
I couldn't figure out an easy way to trace back the position of each character (another win for the obfuscation!) so I decided to let the python script figure it out.

The principle is:

> 1. Run the binary with a dummy password
> 2. Store the value of the local var that is being checked. Remember, this local var is directly affected by one of the characters of our input password
> 4. Replay the binary again with the dummy password, but this time changing just the first character (from `Z` to `b` for ex)
> 5. Compare the local var with the stored value.
> 6. If they're the same, this is not the character that the binary is looking at. So go ahead and change the next character of the dummy password and repeat.
> 7. If the value changed so we have a bingo!

With this procedure we can determine which character the `if` statement is currently validating.
Now it's time to brute-force this character and try every printable ASCII.

Once we find the character that passes the validation, we update the dummy password with the right character in the right place.

With this updated dummy password we repeat the process all over again.

At each iteration our dummy password becomes less and less dummy. Until, 32 iterations later, it's not dummy anymore!

Here is how the sequence looks like:

```
ZZZZZZZZZZZhZZZZZ_ZZZZZZZZZZZZZZ
ZZZZZZZZZZZhZZZZZ_ZZZZZZ5ZOZZZZZ
ZZZZZZZZZZZhZZZZZ_ZZeZZZ5ZOZ4ZZZ
ZZZZZZZZZZZhZZZZZ_ZZeZ5Z5ZOZ4ZZq
ZZZZZZZZZZZhZZZZZ_ZZeZ5Z5eOZ4Z6q
ZZZZnZZZZZZhZZZ3Z_ZZeZ5Z5eOZ4Z6q
ZZmZnZZZZZZhZZZ3l_ZZeZ5Z5eOZ4Z6q
Z1mZnZZZZZZhZZZ3l_ZWeZ5Z5eOZ4Z6q
Z1mZnZZ1ZeZhZZZ3l_ZWeZ5Z5eOZ4Z6q
Z1mZnZS1ZeZhaZZ3l_ZWeZ5Z5eOZ4Z6q
Z1mZnZS1ZeZhaZZ3l_NWeA5Z5eOZ4Z6q
Z1minZS1ZeZhaZZ3l_NWeA5Z5eOZ4P6q
t1minZS1ZeZhaZZ3l_NWeA525eOZ4P6q
t1minZS1ZeChaZn3l_NWeA525eOZ4P6q
t1mingS1ZeChaZn3l_NWeA525eOE4P6q
```

And the output of the script looks something like this:

```
$ ./hack_checkpass.py
Searching char to crack:        
--------------------
ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
--------------------
bZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
--------------------
ZbZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
--------------------
ZZbZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
--------------------
ZZZbZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
--------------------
ZZZZbZZZZZZZZZZZZZZZZZZZZZZZZZZZ
--------------------
ZZZZZbZZZZZZZZZZZZZZZZZZZZZZZZZZ
--------------------
ZZZZZZbZZZZZZZZZZZZZZZZZZZZZZZZZ
--------------------
ZZZZZZZbZZZZZZZZZZZZZZZZZZZZZZZZ
--------------------
ZZZZZZZZbZZZZZZZZZZZZZZZZZZZZZZZ
--------------------
ZZZZZZZZZbZZZZZZZZZZZZZZZZZZZZZZ
--------------------                                                                                                   
ZZZZZZZZZZbZZZZZZZZZZZZZZZZZZZZZ
--------------------
ZZZZZZZZZZZbZZZZZZZZZZZZZZZZZZZZ
Index of next char to crack:  11
Burteforcing char...            
--------------------
ZZZZZZZZZZZ0ZZZZZZZZZZZZZZZZZZZZ
--------------------
ZZZZZZZZZZZ1ZZZZZZZZZZZZZZZZZZZZ
--------------------
ZZZZZZZZZZZ2ZZZZZZZZZZZZZZZZZZZZ
--------------------
ZZZZZZZZZZZ3ZZZZZZZZZZZZZZZZZZZZ    
--------------------                                                                                                   
ZZZZZZZZZZZ4ZZZZZZZZZZZZZZZZZZZZ 

< SKIPPED SOME LINES>

--------------------
ZZZZZZZZZZZgZZZZZZZZZZZZZZZZZZZZ
--------------------
ZZZZZZZZZZZhZZZZZZZZZZZZZZZZZZZZ
Cracked char! So far password is:  ZZZZZZZZZZZhZZZZZZZZZZZZZZZZZZZZ
Searching char to crack:
--------------------
ZZZZZZZZZZZhZZZZZZZZZZZZZZZZZZZZ
--------------------
bZZZZZZZZZZhZZZZZZZZZZZZZZZZZZZZ
--------------------
ZbZZZZZZZZZhZZZZZZZZZZZZZZZZZZZZ
--------------------
ZZbZZZZZZZZhZZZZZZZZZZZZZZZZZZZZ

< SKIPPED MANY... MANY... MANY LINES>

--------------------                
t1mingS1deChaln3l_NWeA525eOE4P6q
--------------------                                                                                                   
t1mingS1deChamn3l_NWeA525eOE4P6q
--------------------                                                                                                   
t1mingS1deChann3l_NWeA525eOE4P6q                                                                                   
Cracked char! So far password is: t1mingS1deChann3l_NWeA525eOE4P6q


Final Password: 
t1mingS1deChann3l_NWeA525eOE4P6q
```

And the more important test:

```
$ ./checkpass picoCTF{t1mingS1deChann3l_NWeA525eOE4P6q}
Success
```

You can check the script [here](hack_checkpass.py).
