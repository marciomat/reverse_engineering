> source: https://crackmes.one/crackme/611e76ec33c5d45db85dc2d1

# Tools used

- radare2

# Files

Input:
- [exatlon_v1](exatlon_v1) - Binary to crack

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

The first thing to realize is that this file is compressed with UPX. Before I learned that it was very difficult to reverse engineer this binary since radare2 (and any other tool) won't be able to show a very readable structure.

One way to check for this compression is by running the command `strings` and `grep` for _UPX_:

```
$ strings exatlon_v1 | grep UPX                                                                                                                                                                                                      130 ⨯
UPX!<
$Info: This file is packed with the UPX executable packer http://upx.sf.net $
$Id: UPX 3.95 Copyright (C) 1996-2018 the UPX Team. All Rights Reserved. $
UPX!u
UPX!
UPX!
```
