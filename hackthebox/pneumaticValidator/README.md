> source: [https://app.hackthebox.com/challenges/pneumatic-validator](https://app.hackthebox.com/challenges/pneumatic-validator)

# Files

Input:
- [pneumaticvalidator](pneumaticvalidator) - Original binary to crack
- [crack_passw.py](https://github.com/marciomat/reverse_engineering/tree/main/hackthebox/pneumaticValidator/crack_passw.py) - Python script to decrypt the password

Output:
- [main.md](https://github.com/marciomat/reverse_engineering/tree/main/hackthebox/pneumaticValidator/main.md) - Full C decompilation of the `main()` function

# The challenge

When we run the binary, it asks for the password to be passed as an argument.
And the first thing it does is validate the legnth:

```
$ ./pneumaticvalidator myPasswordAttempt   
Starting the Pneumatic Flag Validation Machine...
Wrong length
```

After opening the binary we can easily see that we need 20 characters.
And this is what we get with the right lenght:

```
$ ./pneumaticvalidator myPasswordAttempt012
Starting the Pneumatic Flag Validation Machine...
Initializing Simulation...
Simulating...
Wrong \o\
```

# Solution

This challenge is quite hard. It has a very long and complex validation 