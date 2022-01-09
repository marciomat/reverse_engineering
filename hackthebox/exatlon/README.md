> source: https://app.hackthebox.com/challenges/exatlon

# Tools used

- radare2

# Files

Input:
- [exatlon_v1](exatlon_v1) - Binary to crack

Output:
- [disassembly.md](disassembly.md) - Full disassembly of the `main()` function

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

---

Now that the binary is decompressed we can open and analyze it in _radare2_:

```
r2 -A exatlon_v1
```

We look for the `main()` function and it's there.

And it's very straightforward to find where it stores the user input:

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

---

Now we have couple of ways to deal with it.

One approach is to try to understand what `exatlon()` is doing.
Another approach is to consider `exatlon()` as a black-box and just look at what goes in and what comes out.

After a quick look at `exatlon()` it was pretty clear that this would be very deep rabbit-hole.
So approach number 2 it is!

---


