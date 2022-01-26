> source: https://crackmes.one/crackme/615888be33c5d4329c344f66

# Tools used

- radare2

# Files

Input:
- [cm001](cm001) - Original binary to crack
- [patched_cm001](patched_cm001) - Patched binary

Output:
- [decode_pass.py](decode_pass.py) - Python script to decrypt the password
- [main.md](main.md) - Full disassembly of the `main()` function
- [fcn_0040152b.md](fcn_0040152b.md) - Full disassembly of the function `fcn.0040152b`

# The challenge

At first glance this seems to be another classic type of crackme. But during the investigation it brought up some unique challenges (and I'm not even sure if that was a bug or a feature!)

```
$ ./cm001 
Input:
mypassword
Failed to validate password
```

# Solution

First we open the binary in _radare2_ for analysis:

```
$ r2 -A cm001
```

We can access the `main()` so we jump there to see what it looks like.

```assembly
│           0x004010b0      55             push rbp
│           0x004010b1      660fefc0       pxor xmm0, xmm0
│           0x004010b5      488d3d700f00.  lea rdi, str.Input:         ; 0x40202c ; "Input:" ; const char *s
│           0x004010bc      4883ec50       sub rsp, 0x50
│           0x004010c0      0f290424       movaps xmmword [rsp], xmm0
│           0x004010c4      4889e5         mov rbp, rsp
│           0x004010c7      0f29442410     movaps xmmword [var_10h], xmm0
│           0x004010cc      0f29442420     movaps xmmword [var_20h], xmm0
│           0x004010d1      0f29442430     movaps xmmword [var_30h], xmm0
│           0x004010d6      c644244000     mov byte [var_40h], 0
│           0x004010db      e850ffffff     call sym.imp.puts           ;[1] ; int puts(const char *s)
│           0x004010e0      488b15a92f00.  mov rdx, qword [obj.stdin]    ; [0x404090:8]=0 ; FILE *stream
│           0x004010e7      be41000000     mov esi, 0x41               ; 'A' ; 65 ; int size
│           0x004010ec      4889ef         mov rdi, rbp                ; char *s
│           0x004010ef      e86cffffff     call sym.imp.fgets          ;[2] ; char *fgets(char *s, int size, FILE *stream) 
```

It's very straightforward and simple. It prints the string `Input:` and reads the string from the user.

> One thing to notice though, is the presence of `xmm0`. Later on we will see why.

---

Next, it starts to process the user input:

```assembly
│           0x004010f4      4889ef         mov rdi, rbp                ; const char *s
│           0x004010f7      e854ffffff     call sym.imp.strlen         ;[3] ; size_t strlen(const char *s)
│           0x004010fc      4889ef         mov rdi, rbp                ; int64_t arg1
│           0x004010ff      89c6           mov esi, eax                ; uint32_t arg2
│           0x00401101      e825040000     call fcn.0040152b           ;[4]                   
```

So `rbp` is pointing to where the user input is stored.

First it calls `strlen()` to get the length of the string passed by the user.

Then the function `fcn.0040152b()` is called with the user input as _arg1_ and the string length as _arg2_.

## fcn.0040152b

