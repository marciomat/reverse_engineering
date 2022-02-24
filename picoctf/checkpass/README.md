> source: [https://play.picoctf.org/practice?page=1&search=checkpass](https://play.picoctf.org/practice?page=1&search=checkpass)

# Files

Input:
- [checkpass](checkpass) - Original binary to crack

Output:
- [hack_checkpass.py](hack_checkpass.py) - Python script used to crack the password
- [main.md](main.md) - Full disassembly of the `main()` function

# The challenge

This binary receives the password input via the first call parameter.
And we have to find the right password:

```
$ ./checkpass password_attempt
Invalid length
```

The first obvious thing to notice is the error message.
It gives us a first clue since it tells us that the legnth is invalid.

So if we feel like bruteforcing it we can try multiple different password until we find the right lenght.
But later on we will find the check in the code.

# Solution


