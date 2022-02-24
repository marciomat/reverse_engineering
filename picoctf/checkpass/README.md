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
      │││   0x564966c059e0      48b87069636f.  movabs rax, 0x7b4654436f636970    ; 'picoCTF{'
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

From my comments we can see where it checks for the password lenght (41) and also checks if the password starts with `picoCTF{` and ends with `}`.

So now we know how the password has to look like, and we also know that the actual password will have 32 characters (41 - `picoCTF{}`).