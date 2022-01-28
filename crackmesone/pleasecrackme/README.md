
> source: https://crackmes.one/crackme/612e85d833c5d41acedffa4f

# Files

Input:
- [612e85d833c5d41acedffa4f.zip](612e85d833c5d41acedffa4f.zip) - Original crackmesone file
- [PleaseCrackMe](PleaseCrackMe) - Binary to crack

Output:
- [disassembly.md](disassembly.md) - Full disassembly of `main()` function


# The challenge

This challenge is very simple.
We need to find the correct password, which is generated at run-time.

```
$ ./PleaseCrackMe 
Type in your Username: Bob

Type in a number beetween 1 and 9: 7

Type in the password: myPass

Wrong password

```

# Solution

As always we start by opening and analyzing the binary in radare2:

```
r2 -A PleaseCrackMe
```

We have access to the `main()` function, so we `seek` to it right away:

> I've renamed local variables and added some comments for clarity

```assembly
│           0x00001211      e8bafeffff     call sym.imp.printf
│           0x00001216      488d4590       lea rax, [input_name]
│           0x0000121a      4889c6         mov rsi, rax             ; rsi = &input_name
│           0x0000121d      488d3dfc0d00.  lea rdi, [0x00002020]    ; "%s" ; const char *format
│           0x00001224      b800000000     mov eax, 0
│           0x00001229      e8c2feffff     call sym.imp.__isoc99_scanf  ; read input_name from user
│           0x0000122e      488d3df30d00.  lea rdi, str._nType_in_a_number_beetween_1_and_9:_
│           0x00001235      b800000000     mov eax, 0
│           0x0000123a      e891feffff     call sym.imp.printf
│           0x0000123f      488d4588       lea rax, [input_number]
│           0x00001243      4889c6         mov rsi, rax             ; rsi = &input_number
│           0x00001246      488d3d000e00.  lea rdi, [0x0000204d]    ; "%d" ; const char *format
│           0x0000124d      b800000000     mov eax, 0
│           0x00001252      e899feffff     call sym.imp.__isoc99_scanf  ; read input_number from user
```

---

At this point we know where it keeps the user's input: `input_name` and `input_number`.

Next it checks for the correct range for the `input_number`.

```assembly
│           0x00001257      8b4588         mov eax, dword [input_number]
│           0x0000125a      85c0           test eax, eax
│       ┌─< 0x0000125c      7f16           jg 0x1274
│       │   0x0000125e      488d3deb0d00.  lea rdi, str._nError:_Number_is_too_small
│       │   0x00001265      e836feffff     call sym.imp.puts
│       │   0x0000126a      b8ffffffff     mov eax, 0xffffffff         ; -1 (error code)
│      ┌──< 0x0000126f      e9bd000000     jmp 0x1331
│      ││   ; CODE XREF from main @ 0x127
│      │└─> 0x00001274      8b4588         mov eax, dword [input_number]
│      │    0x00001277      83f809         cmp eax, 9
│      │┌─< 0x0000127a      7e16           jle 0x1292
│      ││   0x0000127c      488d3de90d00.  lea rdi, str._nError:_Number_is_too_big
│      ││   0x00001283      e818feffff     call sym.imp.puts
│      ││   0x00001288      b8ffffffff     mov eax, 0xffffffff         ; -1 (error code)
│     ┌───< 0x0000128d      e99f000000     jmp 0x1331
```

As we can imagine, `jmp 0x1331` goes to the end of the execution and the program terminates returning (-1).

---

Next is where it generates the password (that the user has to match).
See the section below with comments and renamed local variables:

> It doesn't show in the code below but `rbp-0x50` is now renamed as `gen_password` since this is the local variable where it keeps the newly generated password

```assembly
│     ││└─> 0x00001292      c7458c000000.  mov dword [loop_i], 0    ; initial condition
│     ││┌─< 0x00001299      eb20           jmp 0x12bb
│     │││   ; CODE XREF from main @ 0x12d0      
│    ┌────> 0x0000129b      8b458c         mov eax, dword [loop_i]
│    ╎│││   0x0000129e      4898           cdqe
│    ╎│││   0x000012a0      0fb6440590     movzx eax, byte [rbp + rax - 0x70] ; eax = input_name[i_loop]
│    ╎│││   0x000012a5      89c2           mov edx, eax
│    ╎│││   0x000012a7      8b4588         mov eax, dword [input_number]    ; eax = input_number
│    ╎│││   0x000012aa      01d0           add eax, edx     ; eax = input_name[i_loop] + input_number
│    ╎│││   0x000012ac      89c2           mov edx, eax
│    ╎│││   0x000012ae      8b458c         mov eax, dword [loop_i]
│    ╎│││   0x000012b1      4898           cdqe
│    ╎│││   0x000012b3      885405b0       mov byte [rbp + rax - 0x50], dl ; gen_password[i_loop] = input_name[i_loop] + input_number
│    ╎│││   0x000012b7      83458c01       add dword [loop_i], 1           ; i_loop ++
│    ╎│││   ; CODE XREF from main @ 0x1299
│    ╎││└─> 0x000012bb      8b458c         mov eax, dword [loop_i]
│    ╎││    0x000012be      4863d8         movsxd rbx, eax
│    ╎││    0x000012c1      488d4590       lea rax, [input_name]
│    ╎││    0x000012c5      4889c7         mov rdi, rax
│    ╎││    0x000012c8      e8e3fdffff     call sym.imp.strlen
│    ╎││    0x000012cd      4839c3         cmp rbx, rax
│    └────< 0x000012d0      72c9           jb 0x129b    ; while (i_loop < strlen(input_name))
```

So, in summary, it takes each _char_ from `input_name` and adds up with `input_number`. Then stores it in `gen_password`.

Simple enough?

**There's one catch!** There's a bug in the code above and we will come back to it later on.

---

Now for the section where it reads the password and verifies it.

```assembly
│           0x000012d2      488d3dad0d00.  lea rdi, str._nType_in_the_password:_
│           0x000012d9      b800000000     mov eax, 0
│           0x000012de      e8edfdffff     call sym.imp.printf
│           0x000012e3      488d45d0       lea rax, [input_password]    ; rax = &input_password
│           0x000012e7      4889c6         mov rsi, rax
│           0x000012ea      488d3d2f0d00.  lea rdi, [0x00002020]
│           0x000012f1      b800000000     mov eax, 0
│           0x000012f6      e8f5fdffff     call sym.imp.__isoc99_scanf
│           0x000012fb      488d55d0       lea rdx, [input_password]
│           0x000012ff      488d45b0       lea rax, [gen_password]
│           0x00001303      4889d6         mov rsi, rdx                ; const char *s2
│           0x00001306      4889c7         mov rdi, rax                ; const char *s1
│           0x00001309      e8d2fdffff     call sym.imp.strcmp         ; strcmp(gen_password, input_password)
│           0x0000130e      85c0           test eax, eax
│       ┌─< 0x00001310      750e           jne 0x1320
```

If the strings `gen_password` and `input_password` are equal, we have cracked it!

So from the previous section we know that `gen_password` is basically our `input_name` but with each _char_ added by `input_number`.

Examples of valid combinations:

input_name | input_number | gen_password
---|---|---
abc | 2 | cde
ggg | 1 | hhh
l | 1 | m

and so on...

So let's try!

```
$ ./PleaseCrackMe
Type in your Username: abc

Type in a number beetween 1 and 9: 2

Type in the password: cde

Wrong password
```

It failed!

# There is a bug in the binary!

Let's look closer to understand what's going on. 

First we need to understand how `strcmp()` works.

> This function starts comparing the first character of each string. If they are equal to each other, it continues with the following pairs until the characters differ or _until a terminating null-character is reached_.

The key part is:

> until a terminating null-character is reached

And if we look back in the code that generates `gen_password`, it doesn't add the `NULL` character at the end of the string.
This messes up with `strcmp()` and creates a non-deterministic behavior in the code.

To show the lack of determinism, let's try a long sequence of characters and see if we get lucky:

```
$ ./PleaseCrackMe
Type in your Username: aaaaaa

Type in a number beetween 1 and 9: 1

Type in the password: bbbbbb

You are succesfully logged in
```

So now we got lucky and by chance our string in `gen_password` ended up terminated by `NULL` (i.e. the byte `0x00` happened to be located right after the sequence of chars `bbbbbb`)

And to prove it, we can run the binary, put a breakpoint after `gen_passowrd` is created and check its content.

As input I've used:

```
input_name: a
input_number: 1
```

And after `gen_password` is filled out by the logic above, we have this in memory: 

```
:> px 10 @ rbp-0x50
- offset -       0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x7fffbe192e40  622e 19be ff7f 0000 9c95                 b.........
```

We can see the first character is `b` (which is correct since it's `"a" + 1`), but following it there are 5 random characters (garbage memory).

And if we repeat the process for a longer string, in the hopes that we pass 'over' the garbage memory, we can have this:

```
:> px 10 @ rbp-0x50
- offset -       0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x7fffbe192e40  6262 6262 6262 0000 9c95                 bbbbbb....
```

In this case we have a _pass_.

So lesson's learned: Whenever we manually create a string, we should always play safe and terminate it with a `NULL` char.

That's all for today!
