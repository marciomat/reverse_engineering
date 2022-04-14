> source: [https://app.hackthebox.com/challenges/headache](https://app.hackthebox.com/challenges/headache)

# Files

Input:
- [headache](headache) - Original binary to crack

Output:
- [patched_headache](patched_headache) - Patched version to help debug, bypassing checks

# The challenge

From the outside it looks just like any other CTF challenge:

```
$ ./headache                           
Initialising.....
Enter the key: abcde
Login Failed!
```

But on the inside this challenge is a beast!

# Solution

This binary uses 2 main tricks to hide the flag:

- It uses `ptrace` calls (in more than one place) to check if a debugger is being used to change its behavior.
- And it also modifies itself at runtime. The `main()` function is decrypted right before being called.

> For more information on how `ptrace` is used to detect a debugger, check my write-up for [bombsLanded](../bombsLanded#debugger-protection)
