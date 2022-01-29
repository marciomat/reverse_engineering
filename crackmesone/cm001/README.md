> source: [https://crackmes.one/crackme/615888be33c5d4329c344f66](https://crackmes.one/crackme/615888be33c5d4329c344f66)

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

This function `fcn.0040152b()` is the last thing done in `main()` (apart from restoring the stack and returning).
So clearly this is where our password is being validated.

Let's take a closer look at it:

```assembly
┌ 351: fcn.0040152b (int64_t arg1, uint32_t arg2, int64_t arg5, int64_t arg7, int64_t arg9, int64_t arg10);
│           ; arg int64_t arg1 @ dh
│           ; arg uint32_t arg2 @ edx
│           ; arg int64_t arg5 @ mm2
│           ; arg int64_t arg7 @ af
│           ; arg int64_t arg9 @ esp
│           ; arg int64_t arg10 @ ymm5
│           0x0040152b      83fe40         cmp esi, 0x40               ; elf_phdr ; arg2
│           0x0040152e      48893c25a040.  mov qword [0x4040a0], rdi    ; [0x4040a0:8]=0 ; arg1
│       ┌─< 0x00401536      0f854e010000   jne fcn.0040168a
```

The first instruction is comparing `esi` with `0x40`.

As per the [calling convention](https://en.wikipedia.org/wiki/X86_calling_conventions) we know that `esi` is the second argument. And by looking at the function call we see that string length was passed via `esi`.

If `esi` is not equal to `0x40` it jumps to `fcn.0040168a`.

```assembly
┌ 155: fcn.0040168a ();
│      └└─> 0x0040168a      48c7c0010000.  mov rax, 1
│           0x00401691      48c7c7010000.  mov rdi, 1
│           0x00401698      48c7c6604040.  mov rsi, str.Failed_to_validate_password_n    ; 0x404060 ; "Failed to validate password\n"
│           0x0040169f      48c7c21c0000.  mov rdx, 0x1c               ; 28
│           0x004016a6      0f05           syscall
```

Now we know that `fcn.0040168a` is where it jumps whenever the validation of the password fails.
We can rename this function to `failed_password()` using the following command in radare2:

`afn failed_password`

So coming back to the first validation of string lenght. It has to be equal to `0x40`, which means 64 in decimal.

## Stage 1: Validating the first group of 16 characters

Next we have a huge sequence of commands followed by another `cmp` and `jne failed_password`.

Let's take a look at the first part:

```assembly
│       │   0x0040153c      660f1007       movupd xmm0, xmmword [rdi]
│       │   0x00401540      660f104f10     movupd xmm1, xmmword [rdi + 0x10]
│       │   0x00401545      660f105720     movupd xmm2, xmmword [rdi + 0x20]
│       │   0x0040154a      660f105f30     movupd xmm3, xmmword [rdi + 0x30]
│       │   0x0040154f      660fef042580.  pxor xmm0, xmmword [str.dG46rskj8_457_:]    ; arg7
```

First thing to remember is that `rdi` (first argument of the function) is pointing to where the user input is stored.

So the first four lines are copying all 64 characaters from the user input to the registers `xmm0`, `xmm1`, `xmm2`, `xmm3`.

> Note: These registers `xmm` are 128-bit and normally used for floating-point math.
>
> But here they're used to store the very long password.

Then it takes the first 16 characters (i.e. `xmm0`) and performs a XOR operation with some hardcoded data:

```
:> px 16 @ str.dG46rskj8_457_:
- offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x00404080  6447 3436 7273 6b6a 382d 3435 3728 7e3a  dG46rskj8-457(~:
```

This is probably some random (but hardcoded) sequence of bytes used to just scramble a bit our password.

Let's keep this in mind and keep moving forward:

```assembly
│       │   0x00401558      31c0           xor eax, eax
│       │   0x0040155a      66410f3a14c0.  pextrb r8d, xmm0, 0
│       │   0x00401561      4431c0         xor eax, r8d                ; arg5
│       │   0x00401564      66410f3a14c0.  pextrb r8d, xmm0, 1
│       │   0x0040156b      4431c0         xor eax, r8d                ; arg5
│       │   0x0040156e      66410f3a14c0.  pextrb r8d, xmm0, 2
│       │   0x00401575      4431c0         xor eax, r8d                ; arg5
│       │   0x00401578      66410f3a14c0.  pextrb r8d, xmm0, 3
│       │   0x0040157f      4431c0         xor eax, r8d                ; arg5
│       │   0x00401582      66410f3a14c0.  pextrb r8d, xmm0, 4
│       │   0x00401589      4431c0         xor eax, r8d                ; arg5
│       │   0x0040158c      66410f3a14c0.  pextrb r8d, xmm0, 5
│       │   0x00401593      4431c0         xor eax, r8d                ; arg5
│       │   0x00401596      66410f3a14c0.  pextrb r8d, xmm0, 6
│       │   0x0040159d      4431c0         xor eax, r8d                ; arg5
│       │   0x004015a0      66410f3a14c0.  pextrb r8d, xmm0, 7
│       │   0x004015a7      4431c0         xor eax, r8d                ; arg5
│       │   0x004015aa      66410f3a14c0.  pextrb r8d, xmm0, 8
│       │   0x004015b1      4431c0         xor eax, r8d                ; arg5
│       │   0x004015b4      66410f3a14c0.  pextrb r8d, xmm0, 9
│       │   0x004015bb      4431c0         xor eax, r8d                ; arg5
│       │   0x004015be      66410f3a14c0.  pextrb r8d, xmm0, 0xa
│       │   0x004015c5      4431c0         xor eax, r8d                ; arg5
│       │   0x004015c8      66410f3a14c0.  pextrb r8d, xmm0, 0xb
│       │   0x004015cf      4431c0         xor eax, r8d                ; arg5
│       │   0x004015d2      66410f3a14c0.  pextrb r8d, xmm0, 0xc
│       │   0x004015d9      4431c0         xor eax, r8d                ; arg5
│       │   0x004015dc      66410f3a14c0.  pextrb r8d, xmm0, 0xd
│       │   0x004015e3      4431c0         xor eax, r8d                ; arg5
│       │   0x004015e6      66410f3a14c0.  pextrb r8d, xmm0, 0xe
│       │   0x004015ed      4431c0         xor eax, r8d                ; arg5
│       │   0x004015f0      66410f3a14c0.  pextrb r8d, xmm0, 0xf
│       │   0x004015f7      4431c0         xor eax, r8d                ; arg5
│       │   0x004015fa      83f800         cmp eax, 0
│      ┌──< 0x004015fd      0f8587000000   jne failed_password
```

The first instruction is a common way to reset (zero) a register. So `eax` is reset and then a long sequence of operations are executed.

Let's look closer into the first few instructions to understand what's going on:

```assembly
│       │   0x0040155a      66410f3a14c0.  pextrb r8d, xmm0, 0
│       │   0x00401561      4431c0         xor eax, r8d                ; arg5
```

The instruction `pextrb` is basically extracting a byte from `xmm0` and copying into `r8d`.
But which byte? The last operand defines which one (in this case it's 0, so the least significant byte).

So the first byte from `xmm0` is copied to `r8d` and then it's XORed with `eax`.
And this sequence is executed 16 times, each time extracting the next byte from `xmm0`.

At the end, the content of `eax` (which accumulates throughout the entire sequence) has to be equal to zero, otherwise the password validation fails.

>This is very interesting, and by now we should already expect that a script will have to brute-force this sequence of 16 characters that can produce the desired result.

## Stage 2: Validating the second group of 16 characters

Assuming we survived so far, next we have some more random magic numbers math:

```assembly
│       │   0x00401603      48c7c0110000.  mov rax, 0x11               ; 17
│       │   0x0040160a      4801c0         add rax, rax
│       │   0x0040160d      4d31c0         xor r8, r8
│       │   0x00401610      66410f3a14c0.  pextrb r8d, xmm0, 0xb
│       │   0x00401617      490fafc0       imul rax, r8
│       │   0x0040161b      4801c0         add rax, rax
│       │   0x0040161e      4801c0         add rax, rax
│       │   0x00401621      48053a010000   add rax, 0x13a              ; 314
```

First thing to notice is that the content of `eax` from the last stage is not used here since it got overwritten with `0x11` in the first line above.

It's not hard to follow what the code is doing, we just need some patience to go line by line since it's all simple bits and bytes bein moved around. And the final result is stored in `rax`.

One important detail is to realize that it still uses the byte number 11 (`0xb`) from the `xmm0`. So even though we're now validating the second group of 16 characters, the content of `xmm0` still influences here.

> And be aware that the content of `xmm0` here is after it got XORed with that hardcoded sequence of random bytes (`str.dG46rskj8_457_:`).

---

Now the binary finally starts looking at the second group of 16 characters (i.e. the content of `xmm1`).

```assembly
│       │   0x00401627      660f110c25b0.  movupd xmmword [0x4040b0], xmm1
│       │   0x00401630      4831c9         xor rcx, rcx
│       │   0x00401633      49c7c0b04040.  mov r8, 0x4040b0
│       │   0x0040163a      4831db         xor rbx, rbx
│       │   ; CODE XREF from fcn.0040152b @ 0x40164a
│      ┌──> 0x0040163d      418a1c08       mov bl, byte [r8 + rcx]
│      ╎│   0x00401641      4829d8         sub rax, rbx
│      ╎│   0x00401644      48ffc1         inc rcx
│      ╎│   0x00401647      83f910         cmp ecx, 0x10               ; 16
│      └──< 0x0040164a      75f1           jne 0x40163d
│       │   0x0040164c      4883f800       cmp rax, 0
│      ┌──< 0x00401650      7538           jne failed_password
```

Here we have a loop with `rcx` as the counter. The loop counts up to `0x10` (so 16 times).

We can also see that `r8` contains the part of our password that was stored in `xmm1` (so characters from 16 to 31).

Both `rcx` and `rbx` are reset right before the loop begins.

In the first line of the loop we have the following instruction:

```assembly
mov bl, byte [r8 + rcx]
```

This is a common way to access the data pointed by `r8`, byte per byte, with each byte indexed by the counter `rcx`. And each byte is stored in `bl`.

Again, more 'random' logic moving bytes around for each iteration of the loop. Remember, the loop has a counter from `0x00` to `0x10` (`0x10` not included in the iteration, so it loops 16x).

And in the end, the accumulated result in `rax` shall be equal to zero, otherwise it fails.

## Stage 2 and a half: A bug? Or a feature?

Now it's where I got stuck for a long time. I'm still not sure if I'm missing something or there's a bug in the code.

Let's take a look:

```assembly
│      ││   0x00401652      66480f7ed8     movq rax, xmm3              ; arg10
│      ││   0x00401657      66480f3a16d3.  pextrq rbx, xmm2, 1
│      ││   0x0040165e      4831d8         xor rax, rbx
│      ││   0x00401661      48bb031223ff.  movabs rbx, 0xffff231203
│      ││   0x0040166b      66490f3a16d8.  pextrq r8, xmm3, 1
│      ││   0x00401672      66490f7ed1     movq r9, xmm2               ; arg9
│      ││   0x00401677      4c890c25b040.  mov qword [0x4040b0], r9    ; [0x4040b0:8]=0
│      ││   0x0040167f      4c890425a840.  mov qword [0x4040a8], r8    ; [0x4040a8:8]=0
└      ││   0x00401687      48f7f3         div rbx
```

The following instruction right after `div rbx` (not shown here) is where the `failed_password()` function starts so it's definetely not part of the normal flow.

Not sure why the last instruction of this function would end with `div rbx`.

Anyways, after days banging my head against the wall I found another piece of code that really seems to be the continuation of the above block of code:

```assembly
            0x004013e0      488b3dc92c00.  mov rdi, qword [0x004040b0]    ; [0x4040b0:8]
            0x004013e7      4c8b05ba2c00.  mov r8, qword [0x004040a8]    ; [0x4040a8:8]
            0x004013ee      55             push rbp
            0x004013ef      4c39c7         cmp rdi, r8
        ┌─< 0x004013f2      0f84c8000000   je 0x4014c0
        │   ; CODE XREF from fcn.00401200 @ +0x2d3
        │   0x004013f8      4883ff0f       cmp rdi, 0xf                ; 15
       ┌──< 0x004013fc      0f878e000000   ja 0x401490
```

And the reason why I believe this should be the continuation is because it's recovering data saved in these 2 memory addresses:
`0x004040b0` and `0x004040a8`. And then it proceeds to run some more validation on that data.

But if you look at the instruction addresses, they're note close by! So we need a jump somewhere to make what I belive is the flow it should take.

The only solution I came up with was to sneak in a jump instruction to replace the `div rbx` opcode above.

But if you look at the opcode for `div rbx`, it's quite small: `0x48f7f3`. So my jump opcode had to fit in there. And a regular `jmp 0x004013e0` instruction is too big and wouldn't fit without corrupting the next instructions.

So I first loaded the intended address (`0x004013e0`) into `rbx` and then used the opcode `jmp rbx`.

To visualize the before and after. The first block of code went from this:

<pre>
│      ││   0x00401652      66480f7ed8     movq rax, xmm3              ; arg10
│      ││   0x00401657      66480f3a16d3.  pextrq rbx, xmm2, 1
│      ││   0x0040165e      4831d8         xor rax, rbx
<mark>│      ││   0x00401661      48bb031223ff.  movabs rbx, 0xffff231203</mark>
│      ││   0x0040166b      66490f3a16d8.  pextrq r8, xmm3, 1
│      ││   0x00401672      66490f7ed1     movq r9, xmm2               ; arg9
│      ││   0x00401677      4c890c25b040.  mov qword [0x4040b0], r9    ; [0x4040b0:8]=0
│      ││   0x0040167f      4c890425a840.  mov qword [0x4040a8], r8    ; [0x4040a8:8]=0
<mark>└      ││   0x00401687      48f7f3         div rbx</mark>
</pre>

To this:

<pre>
│      ││   0x00401652      66480f7ed8     movq rax, xmm3              ; arg10
│      ││   0x00401657      66480f3a16d3.  pextrq rbx, xmm2, 1
│      ││   0x0040165e      4831d8         xor rax, rbx
<b>│      ││   0x00401661      48bbe0134000.  movabs rbx, 0x4013e0</b>
│      ││   0x0040166b      66490f3a16d8.  pextrq r8, xmm3, 1
│      ││   0x00401672      66490f7ed1     movq r9, xmm2               ; arg9
│      ││   0x00401677      4c890c25b040.  mov qword [0x4040b0], r9    ; [0x4040b0:8]=0
│      ││   0x0040167f      4c890425a840.  mov qword [0x4040a8], r8    ; [0x4040a8:8]=0
<mark>└      ││   0x00401687      ffe3           jmp rbx
       ││   0x00401689      90             nop</mark>
</pre>

The line where I loaded the destination address into `rbx` is in the 4th line:
```assembly
│      ││   0x00401661      48bbe0134000.  movabs rbx, 0x4013e0
```

And look at how small is the opcode for the `jmp rbx` instruction! I even had to use a `nop` instruction to avoid shifting all the addresses in the binary.

This patched binary I saved separately: [patched_cm001](patched_cm001)

Now we can continue with the flow and finish the validation of the last 2 segments of the password!

## Stage 3: Validating the rest of the password

At this stage I realized that the binary doesn't really look at all the characters from the `xmm2` and `xmm3`.

And it performs a very basic hash with the characters. This part was possible to just manually manipulate the password string manually and get it to pass. Took me less than 10min of try and error. And not worth going through it line by line.

## So what is the password?

As I had mentioned before, the stage 1 and stage 2 perform a very intensive loop over each character from `xmm0` and `xmm1` so it would take a script to basically brute-force to find a sequence of ASCII that would pass those validations.

I created this ugly but functional python script to find me the first half of the password:
[decode_pass.py](decode_pass.py)

This script found this weird sequence of 64 characters:

```
$ ./decode_pass.py                          
password found:
11111111111112-@222222222222222l33333333333333334444444444444444
```

And as I mentioned before, the second half of the password I just cracked by hand with try and error since it was fairly simple and was faster than trying to update my script to brute-force it for me.

The final answer:
```
$ ./patched_cm001 
Input:
11111111111112-@222222222222222l32333333333333334444444444667764
You found the password:
        11111111111112-@222222222222222l32333333333333334444444444667764
```

## One last mistery!

After I found the password, I tried it in the original (unpatched) binary.

I was sure it would crash since my debugger was always crashing at that `div rbx` instruction!

Spoiler alert:

```
$ ./cm001        
Input:
11111111111112-@222222222222222l32333333333333334444444444667764
You found the password:
        11111111111112-@222222222222222l32333333333333334444444444667764
```

I have no clue what's going on here! 

I hope to one day understand it...