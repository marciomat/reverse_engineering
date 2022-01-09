> source: https://app.hackthebox.com/challenges/exatlon

# Tools used

- radare2

# Files

Input:
- [exatlon_v1](exatlon_v1) - Binary to crack

Output:
- [python script](crack_passw.py) - Python script to decrypt the password
- [disassembly.md](disassembly.md) - Full disassembly of the `main()` function (with renamed local variables for clarity)

# The challenge

This challenge requires to find the right password. And the password itself is the flag for the challenge

```
$ ./exatlon_v1

███████╗██╗  ██╗ █████╗ ████████╗██╗      ██████╗ ███╗   ██╗       ██╗   ██╗ ██╗
██╔════╝╚██╗██╔╝██╔══██╗╚══██╔══╝██║     ██╔═══██╗████╗  ██║       ██║   ██║███║
█████╗   ╚███╔╝ ███████║   ██║   ██║     ██║   ██║██╔██╗ ██║       ██║   ██║╚██║
██╔══╝   ██╔██╗ ██╔══██║   ██║   ██║     ██║   ██║██║╚██╗██║       ╚██╗ ██╔╝ ██║
███████╗██╔╝ ██╗██║  ██║   ██║   ███████╗╚██████╔╝██║ ╚████║███████╗╚████╔╝  ██║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═══╝   ╚═╝


[+] Enter Exatlon Password  : 123
[-] ;(
```

# Solution

The first thing to realize is that this file is compressed with UPX.
Before I learned that, it was very difficult to reverse engineer this binary since radare2 (and any other tool) won't be able to show a very readable structure.

One way to check if a binary is using this compression is by running the command `strings` and `grep` for _UPX_:

```
$ strings exatlon_v1 | grep UPX
UPX!<
$Info: This file is packed with the UPX executable packer http://upx.sf.net $
$Id: UPX 3.95 Copyright (C) 1996-2018 the UPX Team. All Rights Reserved. $
UPX!u
UPX!
UPX!
```

And for unpacking it, we use the following command:

```
upx -d exatlon_v1
```

## Preliminary analysis

Now that the binary is decompressed we can open and analyze it in _radare2_:

```
r2 -A exatlon_v1
```

We look for the `main()` function and it's there.

It's very straightforward to find where it stores the user input:

> A local variable was renamed to `user_input` for clarity

```assembly
│           0x00404cf0      488d35d96714.  lea rsi, str.___Enter_Exatlon_Password__:_    ; 0x54b4d0 ; "[+] Enter Exatlon Password  : " ; int64_t arg2
│           0x00404cf7      488d3d82681a.  lea rdi, obj.std::cout      ; 0x5ab580 ; "@^Z" ; int64_t arg1
│           0x00404cfe      e84d370600     call method std::basic_ostream
│           0x00404d03      488d45b0       lea rax, [user_input]
│           0x00404d07      4889c6         mov rsi, rax
│           0x00404d0a      488d3d8f691a.  lea rdi, obj.std::cin       ; 0x5ab6a0
│           0x00404d11      e87a200000     call method std::basic_istream
```

As we can see above, `user_input`'s address is passed over via `rsi` register to store what the user will enter as the password.

---

Next, we have a call to a function called `exatlon()` and it receives 2 parameters (2 local variables that I renamed here):

- `&encrypted_input`: param1, passed via `rdi`
- `&user_input`: param2, passed via `rsi`

```assembly
│       ╎   0x00404d16      488d45d0       lea rax, [encrypted_input]
│       ╎   0x00404d1a      488d55b0       lea rdx, [user_input]
│       ╎   ;-- rip:
│       ╎   0x00404d1e b    4889d6         mov rsi, rdx                ; int64_t arg2
│       ╎   0x00404d21      4889c7         mov rdi, rax                ; int64_t arg1
│       ╎   0x00404d24      e884fdffff     call sym exatlon
```

By the name of the first parameter you can already guess what this function is doing.

But how could we know what this `exatlon()` was up to?
This will become more obvious when we look at what's coming next.

---

```assembly
│       ╎   0x00404d29      488d45d0       lea rax, [encrypted_input]
│       ╎   ;-- rip:
│       ╎   0x00404d2d b    488d35bc6714.  lea rsi, str.1152_1344_1056_1968_1728_816_1648_784_1584_816_1728_1520_1840_1664_784_1632_1856_1520_1728_816_1632_1856_1520_784_1760_1840_1824_816_1584_1856_784_1776_1760_528_528_2000_
│       ╎   0x00404d34      4889c7         mov rdi, rax                ; int64_t arg1
│       ╎   0x00404d37      e8be030000     call method bool std::operator==
```

In this section there's a function call that is receiving 2 parameters:

- `&encrypted_input`: param1 as `rdi`
- `&str.1151_1344....`: param2 as `rsi`

The second parameter is just a hard-coded memory address that seems to point to the encrypted password that the binary is expecting as the right answer.

So now it's clear why in the previous block of code, we can confidently assume that the function `exatlon()` seems to be where our `user_input` is being encrypted.

## Understanding the encryption

Now we have couple of ways to deal with it.

One approach is to try to understand what `exatlon()` is doing.
Another approach is to consider `exatlon()` as a black-box and just look at what goes in and what comes out.

After a quick look at `exatlon()` it was pretty clear that this would be very deep rabbit-hole.
So approach number 2 it is!

---

First we take a look at the, supposedly expected encrypted password.
In order to do that we put a breakpoint at the assembly line where it loads the address of that string into `rsi` and print it:

```
:> ps @ rsi
1152 1344 1056 1968 1728 816 1648 784 1584 816 1728 1520 1840 1664 784 1632 1856 1520 1728 816 1632 1856 1520 784 1760 1840 1824 816 1584 1856 784 1776 1760 528 528 2000
```

As we can see, it's all in ASCII and seems like each sequence of numbers is one _char_.

---

Now let's hope we can see the `exatlon()` function encrypting our `user_input` in something that resembles the numbers above.

Since we know already where `exatlon()` is storing the `encrypted_input`, we just print it after it returns from `exatlon()`. For this run I used as `user_input`: "0123456789"

And this is what we got:

```
:> pf S @ rax
0x7ffcd7c56d00 = 0x7ffcd7c56d00 -> 0x02378fe0 "768 784 800 816 832 848 864 880 896 912 "
```

> The method to print the strings from `rax` is different since in this case `rax` hold the address to where our encrypted input is stored.
>
> So we used the `pf S` which is a print with a format-string. And the format given is `S` which means: _64bit pointer to string_

And that string seems to be in the same format as the expected password encryption. We can tell that since we have already some hits (meaning, our encrypted password contains numbers in it).

## Decrypting the flag!

The hard part is done. Now we just need to grab the output of `exatlon()` while using as `user_input` a string with all printable ASCII chars.
In doing that we will have a direct map of each ASCII char and its corresponding encrypted code.

After some work we have:

```python
allchars = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}"

allcodes = [528, 544, 560, 576, 592, 608, 624, 640, 656, 672, 688, 704, 720, 736, 752, 768, 784, 800, 816, 832, 848, 864, 880, 896, 912, 928, 944, 960, 976, 992, 1008, 1024, 1040, 1056, 1072, 1088, 1104, 1120, 1136, 1152, 1168, 1184, 1200, 1216, 1232, 1248, 1264, 1280, 1296, 1312, 1328, 1344, 1360, 1376, 1392, 1408, 1424, 1440, 1456, 1472, 1488, 1504, 1520, 1536, 1552, 1568, 1584, 1600, 1616, 1632, 1648, 1664, 1680, 1696, 1712, 1728, 1744, 1760, 1776, 1792, 1808, 1824, 1840, 1856, 1872, 1888, 1904, 1920, 1936, 1952, 1968, 1984, 2000]
```

And we can also grab the encrypted flag that we have already found:

```python
encrpt_pass = [1152, 1344, 1056, 1968, 1728, 816, 1648, 784, 1584, 816, 1728, 1520, 1840, 1664, 784, 1632, 1856, 1520, 1728, 816, 1632, 1856, 1520, 784, 1760, 1840, 1824, 816, 1584, 1856, 784, 1776, 1760, 528, 528, 2000]
```

Using this data structures we can create a simple [python script](crack_passw.py) to decode our flag!
