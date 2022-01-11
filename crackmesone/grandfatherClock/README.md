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

This is a classic CrackMe with an encoded password inside the binary. The password is the flag for the challenge

```
$ ./grandfather_clock my_flag
That's not the flag!
```

# Solution

