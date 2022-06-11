> source: [https://app.hackthebox.com/challenges/teleport](https://app.hackthebox.com/challenges/teleport)

# Files

Input:
- [teleport](teleport) - Original binary to crack

Output:
- [main.md](https://github.com/marciomat/reverse_engineering/tree/main/hackthebox/teleport/main.md) - Full disassembly of the `main()` function
- [setjmp_funcs.md](https://github.com/marciomat/reverse_engineering/tree/main/hackthebox/teleport/setjmp_funcs.md) - List of special functions found in the binary
- [movzx.txt](https://github.com/marciomat/reverse_engineering/tree/main/hackthebox/teleport/movzx.txt) - Parsed data from the 42 `setjmp()` special functions
- [decrypt.py](https://github.com/marciomat/reverse_engineering/tree/main/hackthebox/teleport/decrypt.py) - Python script to decode the flag

# The challenge

This binary has some neat tricks to make it harder to follow the flow.
Makes justice to its name!

```
$ ./teleport my_password_attempt_1
Something's wrong...
```

# Solution

First let's look at how it takes the input password:

```assembly
│           0x0000169e      897dec         mov dword [var_14h], edi    ; argc
│           0x000016a1      488975e0       mov qword [src], rsi        ; argv
│           0x000016a5      837dec02       cmp dword [var_14h], 2
│       ┌─< 0x000016a9      7416           je 0x16c1
│       │   0x000016ab      488d3d620100.  lea rdi, str.Missing_password    ; 0x1814 ; "Missing password" ; const char *s
│       │   0x000016b2      e829f3ffff     call sym.imp.puts           ;[1] ; int puts(const char *s)
│       │   0x000016b7      b8ffffffff     mov eax, 0xffffffff         ; -1
│      ┌──< 0x000016bc      e9c8000000     jmp 0x1789
```

In the code above it is checking if there is an input passed via call argument. If there isn't, it just prints `Missing password` and exits returning `-1`.

Then, considering it found an input, it proceeds to copy it to the address `0x00203280`, like we see below:

```assembly
│      │└─> 0x000016c1      488b45e0       mov rax, qword [src]
│      │    0x000016c5      4883c008       add rax, 8
│      │    0x000016c9      488b00         mov rax, qword [rax]
│      │    0x000016cc      ba64000000     mov edx, 0x64               ; 'd' ; size_t  n
│      │    0x000016d1      4889c6         mov rsi, rax                ; const char *src
│      │    0x000016d4      488d3da51b20.  lea rdi, [0x00203280]       ; char *dest
│      │    0x000016db      e8f0f2ffff     call sym.imp.strncpy
```

## 42: The answer for everything

Now it starts the real part of the puzzle.

We have a loop and `var_8h` is the counter. It loops until the counter gets to `0x2a` in hex, or `42` in decimal.

> This is a soft hint that our password may containt 42 characters, but it's too early to be sure.

```assembly
│      │    0x000016e0      c745f8000000.  mov dword [var_8h], 0
│      │┌─< 0x000016e7      eb23           jmp 0x170c
│      ││   ; CODE XREF from main @ 0x1712
│     ┌───> 0x000016e9      8b45f8         mov eax, dword [var_8h]
│     ╎││   0x000016ec      4898           cdqe
│     ╎││   0x000016ee      488d14c50000.  lea rdx, [rax*8]
│     ╎││   0x000016f6      488d05231920.  lea rax, [0x00203020]
│     ╎││   0x000016fd      488b1402       mov rdx, qword [rdx + rax]
│     ╎││   0x00001701      b800000000     mov eax, 0
│     ╎││   0x00001706      ffd2           call rdx
│     ╎││   0x00001708      8345f801       add dword [var_8h], 1
│     ╎││   ; CODE XREF from main @ 0x16e7
│     ╎│└─> 0x0000170c      8b45f8         mov eax, dword [var_8h]
│     ╎│    0x0000170f      83f82a         cmp eax, 0x2a
│     └───< 0x00001712      76d5           jbe 0x16e9
```

Reading the code more carefully we can also notice that it uses the counter `var_8h` as an index to access values located at the address `0x00203020`.
We can tell that these values are 8 bytes long since the counter to loop is being multiplied by 8.

And finally we also see that the values located at `0x00203020` are addresses that are loaded into `rdx` and then it calls it.

So we have a list of functions that are called in sequence. 42 functions to be precise.

Let's leave this simmering for now. We'll get back to it later.

## First act: The Setup

Here is where the name of this challenge starts to make sense!

In the first 2 lines of the code below we have a function call to `setjmp(env)` (remember that `rdi` is where the first argument of the function is loaded).

```assembly
│           0x00001714      488d3d851a20.  lea rdi, [0x002031a0]       ; jmpbuf env
│           0x0000171b      e8d0f2ffff     call sym.imp._setjmp        ;[2] ; int setjmp(jmpbuf env)
│           0x00001720      8945fc         mov dword [var_4h], eax
│           0x00001723      8b45fc         mov eax, dword [var_4h]
│           0x00001726      83f864         cmp eax, 0x64
│       ┌─< 0x00001729      7407           je 0x1732
│       │   0x0000172b      83f865         cmp eax, 0x65
│      ┌──< 0x0000172e      7410           je 0x1740
│     ┌───< 0x00001730      eb1c           jmp 0x174e
│     │││   ; CODE XREF from main @ 0x1729
│     ││└─> 0x00001732      488d3dec0000.  lea rdi, str.Looks_good_to_me_    ; 0x1825 ; "Looks good to me!" ; const char *s
│     ││    0x00001739      e8a2f2ffff     call sym.imp.puts           ;[3] ; int puts(const char *s)
│     ││┌─< 0x0000173e      eb44           jmp 0x1784
│     │││   ; CODE XREF from main @ 0x172e
│     │└──> 0x00001740      488d3df00000.  lea rdi, str.Somethings_wrong...    ; 0x1837 ; "Something's wrong..." ; const char *s
│     │ │   0x00001747      e894f2ffff     call sym.imp.puts
```

It's very imporant to understand how these `setjmp()` work. So here is a very quick summary:

> It's mechanism consists of 2 parts:
>
> 1. First, `setjmp(jmp_buf env)` saves the context (stack pointer, instruction pointer, registers, etc) into the buffer `env` (which can be any variable passed to the function)
> 2. Then `longjmp(jmp_buf env, int val)` restores the context saved in `env`. Note that since `instruction pointer` is one of the registers saved/restored, it will cause the program flow to jump to where `setjmp()` is located, as if `setjmp()` had just returned. And the returning value of `setjmp()` will be `val`, which was passed to `longjmp(env, val)`.
>
> Note: since the buffer `jmp_buf env` can be any variable passed to these functions, we can have multiple of these context saved in multiple `env` variables.

---

Now we can go back to the 42 functions that we left simmering in the previous section. All those 42 functions were setting up 42 `jmp_buf env` to have them prepared to be restored at some point.

The content of these 42 functions can be found [here](https://github.com/marciomat/reverse_engineering/tree/main/hackthebox/teleport/setjmp_funcs.md).

# Second act: The Confrontation

Now that we understand better the teleporting mechanism, we can look again at the previous code section to get a better analysis.

Here it is again:

```assembly
│           0x00001714      488d3d851a20.  lea rdi, [0x002031a0]       ; jmpbuf env
│           0x0000171b      e8d0f2ffff     call sym.imp._setjmp        ;[2] ; int setjmp(jmpbuf env)
│           0x00001720      8945fc         mov dword [var_4h], eax
│           0x00001723      8b45fc         mov eax, dword [var_4h]
│           0x00001726      83f864         cmp eax, 0x64
│       ┌─< 0x00001729      7407           je 0x1732
│       │   0x0000172b      83f865         cmp eax, 0x65
│      ┌──< 0x0000172e      7410           je 0x1740
│     ┌───< 0x00001730      eb1c           jmp 0x174e
│     │││   ; CODE XREF from main @ 0x1729
│     ││└─> 0x00001732      488d3dec0000.  lea rdi, str.Looks_good_to_me_    ; 0x1825 ; "Looks good to me!" ; const char *s
│     ││    0x00001739      e8a2f2ffff     call sym.imp.puts           ;[3] ; int puts(const char *s)
│     ││┌─< 0x0000173e      eb44           jmp 0x1784
│     │││   ; CODE XREF from main @ 0x172e
│     │└──> 0x00001740      488d3df00000.  lea rdi, str.Somethings_wrong...    ; 0x1837 ; "Something's wrong..." ; const char *s
│     │ │   0x00001747      e894f2ffff     call sym.imp.puts
```

The important thing to notice above is that we have a `setjmp()` call. Which means, a `longjmp()` call somewhere will make the _Instruction Pointer_ jump to this location.

When this jump occurs, it will look for the content of `eax` (remember that `eax` holds the return value from a function call). If `eax` is `0x64` then we have the right password. If it's `0x65` then we have the wrong password. If it's neither one of these 2 values, it will jump to `0x174e`.

Let's see what happens there.

---

Here is the final piece of the puzzle:

```assembly
│     └───> 0x0000174e      8b45fc         mov eax, dword [var_4h]
│      ││   0x00001751      4863d0         movsxd rdx, eax
│      ││   0x00001754      4889d0         mov rax, rdx
│      ││   0x00001757      48c1e002       shl rax, 2
│      ││   0x0000175b      4801d0         add rax, rdx
│      ││   0x0000175e      488d14850000.  lea rdx, [rax*4]
│      ││   0x00001766      4801d0         add rax, rdx
│      ││   0x00001769      48c1e003       shl rax, 3
│      ││   0x0000176d      488d158c1b20.  lea rdx, [0x00203300]
│      ││   0x00001774      4801d0         add rax, rdx
│      ││   0x00001777      be01000000     mov esi, 1                  ; int val
│      ││   0x0000177c      4889c7         mov rdi, rax                ; jmp_buf env
│      ││   0x0000177f      e87cf2ffff     call sym.imp.longjmp        ;[3] ; void longjmp(jmp_buf env, int val)
```

Without going into too many little details, this section is basically preparing an address offset that will be added to the base address `0x00203300`.
Then, the _base address_ + _offset_ will be the address of the `env` buffer passed to `longjmp(env)` call.

Remember those 42 functions that were setting up 42 different `env` buffers? Yeah... you can bet that those buffers are being accessed now!

So we ended up with a loop that starts in this last section of code, then it will jump to one of those 42 functions, which in turn will go back to the main `setjmp()` where it will compare the return value with `0x64` or `0x65`.

And now even without looking at those 42 functions we can guess that it's inside those functions that each character of the password is being validated.

# The final act: The Resolution

For this final act I parsed the ASCII _hex_ value and the position of each character from those 42 functions and wrote a simple python script to output the final flag!

You can see the parsed data [here](https://github.com/marciomat/reverse_engineering/tree/main/hackthebox/teleport/movzx.txt) and the python script [here](https://github.com/marciomat/reverse_engineering/tree/main/hackthebox/teleport/decrypt.py).

Hope you enjoyed!
