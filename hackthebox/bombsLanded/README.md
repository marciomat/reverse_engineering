> source: [https://app.hackthebox.com/challenges/bombs-landed](https://app.hackthebox.com/challenges/bombs-landed)

# Files

Input:
- [BombsLanded](BombsLanded) - Original binary to crack
- [patched_BombsLanded](patched_BombsLanded) - Patched binary

Output:
- [main.md](https://github.com/marciomat/reverse_engineering/tree/main/hackthebox/bombsLanded/main.md) - Full disassembly of the `main()` function

# The challenge

This challenge has some tricky safeguards in place. But on the surface it looks just like any other binary:

```
$ ./BombsLanded     
Bad luck dude.
```

# Solution

At first it looks like this challenge gets its input from the calling argument since at no point it asks for the password.

Let's take a look inside it:

```
$ r2 -A BombsLanded
```

After loading it in radare2 we look for `main()` and jump to it.

```assembly
┌ 432: int main (char **argv);
│           ; var uint32_t var_31h @ ebp-0x31
│           ; var char **var_30h @ ebp-0x30
│           ; var int32_t var_2ch @ ebp-0x2c
│           ; var int32_t var_28h @ ebp-0x28
│           ; var int32_t var_24h @ ebp-0x24
│           ; var int32_t var_20h @ ebp-0x20
│           ; var int32_t var_1ch @ ebp-0x1c
│           ; var int32_t var_10h @ ebp-0x10
│           ; arg char **argv @ esp+0x64
│           0x08048937      8d4c2404       lea ecx, [argv]
│           0x0804893b      83e4f0         and esp, 0xfffffff0
│           0x0804893e      ff71fc         push dword [ecx - 4]
│           0x08048941      55             push ebp
│           0x08048942      89e5           mov ebp, esp
│           0x08048944      57             push edi
│           0x08048945      56             push esi
│           0x08048946      53             push ebx
│           0x08048947      51             push ecx
│           0x08048948      83ec28         sub esp, 0x28
│           0x0804894b      89ca           mov edx, ecx
│           0x0804894d      e87efeffff     call fcn.080487d0
```

The first lines are just setting up the stack.

Then it calls this function `fcn.080487d0`. Let's take a look inside it:

```assembly
┌ 4: fcn.080487d0 ();
│           0x080487d0      8b1c24         mov ebx, dword [esp]
└           0x080487d3      c3             ret
```

It's surprisingly short! Not sure what it is doing at the moment so let's keep moving.

Next there is this long section:

```assembly
│           0x0804894d      e87efeffff     call fcn.080487d0           ;[1]
│           0x08048952      81c3de070000   add ebx, 0x7de              ; 2014 ; section..got.plt ; esi ; esi
│           0x08048958      891d48930408   mov dword [0x8049348], ebx    ; [0x8049348:4]=0; RELOC 32
│           0x0804895e      c745e04c9304.  mov dword [var_20h], 0x804934c   ; RELOC 32
│           0x08048965      c745dc389304.  mov dword [var_24h], 0x8049338   ; RELOC 32
│           0x0804896c      c745d83c9304.  mov dword [var_28h], 0x804933c   ; RELOC 32
│           0x08048973      c745d4409304.  mov dword [var_2ch], 0x8049340   ; RELOC 32
│           0x0804897a      8b45e0         mov eax, dword [var_20h]    ; oeax
│           0x0804897d      8b00           mov eax, dword [eax]        ; oeax
│           0x0804897f      8d4801         lea ecx, [eax + 1]
│           0x08048982      8b45e0         mov eax, dword [var_20h]    ; oeax
│           0x08048985      8908           mov dword [eax], ecx
│           0x08048987      8b45dc         mov eax, dword [var_24h]    ; oeax
│           0x0804898a      8b00           mov eax, dword [eax]        ; oeax
│           0x0804898c      8d48ff         lea ecx, [eax - 1]
│           0x0804898f      8b45dc         mov eax, dword [var_24h]    ; oeax
│           0x08048992      8908           mov dword [eax], ecx
│           0x08048994      8b45d8         mov eax, dword [var_28h]    ; oeax
│           0x08048997      8b00           mov eax, dword [eax]        ; oeax
│           0x08048999      8d4801         lea ecx, [eax + 1]
│           0x0804899c      8b45d8         mov eax, dword [var_28h]    ; oeax
│           0x0804899f      8908           mov dword [eax], ecx
│           0x080489a1      8b45d4         mov eax, dword [var_2ch]    ; oeax
│           0x080489a4      8b00           mov eax, dword [eax]        ; oeax
│           0x080489a6      8d48ff         lea ecx, [eax - 1]
│           0x080489a9      8b45d4         mov eax, dword [var_2ch]    ; oeax
│           0x080489ac      8908           mov dword [eax], ecx
│           0x080489ae      8b45e0         mov eax, dword [var_20h]    ; oeax
│           0x080489b1      8b08           mov ecx, dword [eax]        ; oeax
│           0x080489b3      8b45d8         mov eax, dword [var_28h]    ; oeax
│           0x080489b6      8b00           mov eax, dword [eax]        ; oeax
│           0x080489b8      39c1           cmp ecx, eax                ; esi ; esi
│       ┌─< 0x080489ba      7705           ja 0x80489c1                ; unlikely
│       │   0x080489bc      833a04         cmp dword [edx], 4          ; esi ; esi ; esi
│      ┌──< 0x080489bf      7f57           jg 0x8048a18                ; unlikely
│      ││   ; CODE XREF from main @ 0x80489ba
│      │└─> 0x080489c1      833a03         cmp dword [edx], 3          ; esi ; esi ; esi
│      │┌─< 0x080489c4      7e37           jle 0x80489fd
```

And in the end there are 3 validations happening:

- 1

```assembly
│           0x080489b8      39c1           cmp ecx, eax                ; esi ; esi
│       ┌─< 0x080489ba      7705           ja 0x80489c1                ; unlikely
```

- 2

```assembly
│       │   0x080489bc      833a04         cmp dword [edx], 4          ; esi ; esi ; esi
│      ┌──< 0x080489bf      7f57           jg 0x8048a18                ; unlikely
```

- 3

```assembly
│      │└─> 0x080489c1      833a03         cmp dword [edx], 3          ; esi ; esi ; esi
│      │┌─< 0x080489c4      7e37           jle 0x80489fd
```

After examining all the possibilities, it was clear that the only address that wouldn't show me a "Bad Luck" message is the second one: `0x8048a18`.

So how can we make the binary jump to that address?

The input for this validation is not coming from `argv` or `scanf()` like we'd expect.
Instead, it's all stored in the following addresses:

```
0x804934c
0x8049338
0x804933c
0x8049340
```

## Debugger protection

This part took me days to have any kind of progress. My first thought was that we'd need to perform some kind of stack overflow exploit but couldn't figure out how.

The answer came when I started looking at what happens before the call to `main()`.

For the sake of time I won't go over the entire investigation but after some digging I found this piece of code:

<pre>
            0x08048900      55             push ebp                    ; esp
            0x08048901      89e5           mov ebp, esp
<mark>            0x08048903      c7054c930408.  mov dword [0x804934c], 1</mark>
            0x0804890d      6631c0         xor ax, ax                  ; edi ; edi
            0x08048910      6650           push ax
            0x08048912      6683c001       add ax, 1                   ; edi
            0x08048916      6650           push ax
            0x08048918      6631c0         xor ax, ax                  ; edi ; edi
            0x0804891b      6650           push ax
            0x0804891d      6650           push ax
<mark>            0x0804891f      e8dce6d8ef     call ptrace                 ;[1]; RELOC 32 ptrace ; 0xf7dd7000(0x0, 0x8049130, 0x8049344, 0x8049130)</mark>
            0x08048924      83c408         add esp, 8                  ; edi
            0x08048927      83f8ff         cmp eax, 0xffffffff         ; edi ; edi
        ┌─< 0x0804892a      7507           jne 0x8048933
<mark>        │   0x0804892c      83054c930408.  add dword [0x804934c], 0xa</mark>
        │   ; CODE XREF from eip @ +0x2a
        └─> 0x08048933      90             nop
            0x08048934      90             nop
            0x08048935      5d             pop ebp                     ; edi ; esp
            0x08048936      c3             ret
</pre>

This caught my eyes since it's modifying one of the addresses of interest (`0x804934c`).

It's also calling the syscall `ptrace()` and comparing the returned value with `0xffffffff` (which actually means `-1`).

So what does it mean?
This call to `ptrace()` is probably being used to detect if the binary is being debugged with GDB!

It can be easily tested with this simple code below:

```c
if (ptrace(PTRACE_TRACEME, 0, NULL, 0) == -1) {
    printf("Debugger detected!\n");
} else {
    printf("No debugger detected\n");
}
```

Very sneaky!

## Patching the binary

After that I decided to patch the binary. Specially since I already knew which execution flow I wanted to explore from the `main()` function.

The `main()` went from this:

<pre>
│           0x080489b6      8b00           mov eax, dword [eax]
│           0x080489b8      39c1           cmp ecx, eax
<mark>│       ┌─< 0x080489ba      7705           ja 0x80489c1</mark>
│       │   0x080489bc      833a04         cmp dword [edx], 4
<mark>│      ┌──< 0x080489bf      7f57           jg 0x8048a18</mark>
│      ││   ; CODE XREF from main @ 0x80489ba
│      │└─> 0x080489c1      833a03         cmp dword [edx], 3
│      │┌─< 0x080489c4      7e37           jle 0x80489fd
</pre>

To this:

<pre>
│           0x080489b6      8b00           mov eax, dword [eax]
│           0x080489b8      39c1           cmp ecx, eax
<mark>│           0x080489ba      90             nop
│           0x080489bb      90             nop</mark>
│           0x080489bc      833a04         cmp dword [edx], 4
<mark>│       ┌─< 0x080489bf      eb57           jmp 0x8048a18</mark>
        │   0x080489c1      833a03         cmp dword [edx], 3
       ┌──< 0x080489c4      7e37           jle 0x80489fd
</pre>

> There are many different ways to achive the same goal here, but I wanted to keep as much as possible the same look and feel from the original structure

So with these changes in place we removed all the initial protections from the code.

## Reading the password from the user

So now we're finally at the long-awaited address `0x8048a18`!

At first there's not much going on (at least not that I can understand!).

But eventually we get to this section where it asks for the user's input, printing the string `input password: `

```assembly
            0xf7f7c0af      50             push eax                    ; (pstr 0xff96975b) "input password: "
            0xf7f7c0b0      b8b0860408     mov eax, sym.imp.printf     ; 0x80486b0
            0xf7f7c0b5      ffd0           call eax                    ; sym.imp.printf
            0xf7f7c0b7      83c410         add esp, 0x10
            0xf7f7c0ba      83ec04         sub esp, 4
            0xf7f7c0bd      6a11           push 0x11                   ; 17 ; esp
            0xf7f7c0bf      6a00           push 0
            0xf7f7c0c1      8d4593         lea eax, [ebp - 0x6d]
            0xf7f7c0c4      50             push eax
            0xf7f7c0c5      b850870408     mov eax, sym.imp.memset     ; 0x8048750
            0xf7f7c0ca      ffd0           call eax                    ; sym.imp.memset
            0xf7f7c0cc      83c410         add esp, 0x10
            0xf7f7c0cf      83ec08         sub esp, 8
            0xf7f7c0d2      8d45ba         lea eax, [ebp - 0x46]
            0xf7f7c0d5      50             push eax
            0xf7f7c0d6      8d4590         lea eax, [ebp - 0x70]
            0xf7f7c0d9      50             push eax
            0xf7f7c0da      b860870408     mov eax, sym.imp.__isoc99_scanf    ; 0x8048760
            0xf7f7c0df      ffd0           call eax
```

This is a good sign and means we should be close to where it will validate the password.

## strncmp() saves the day!

We keep going with the flow and we finally get to this call:

```assembly
            0xf7f7c107      b8e78a0408     mov eax, sym.strncmp
            0xf7f7c10c      ffd0           call eax
```

This `strncmp()` is probably a custom-made version of the C-library function. So it's not very obvious that we have to look inside it, but we should!

```assembly
┌ 260: int sym.strncmp (const char *s1, const char *s2, size_t n);
│           ; var int32_t var_18h @ ebp-0x18
│           ; var char *var_14h @ ebp-0x14
│           ; var int32_t var_10h @ ebp-0x10
│           ; var int32_t var_ch @ ebp-0xc
│           ; arg const char *s2 @ ebp+0x8
│           ; arg size_t s1 @ ebp+0xc
│           ; arg uint32_t arg_10h @ ebp+0x10
│           0x08048ae7      55             push ebp
│           0x08048ae8      89e5           mov ebp, esp
│           0x08048aea      83ec18         sub esp, 0x18
│           0x08048aed      83ec08         sub esp, 8
│           0x08048af0      68a28c0408     push 0x8048ca2
│           0x08048af5      6aff           push 0xffffffffffffffff     ; const char *s1
│           0x08048af7      e844d9eaef     call dlsym                  ;[1]; RELOC 32 dlsym
│           0x08048afc      83c410         add esp, 0x10
│           0x08048aff      8945f0         mov dword [var_10h], eax
│           0x08048b02      837d100a       cmp dword [arg_10h], 0xa
│       ┌─< 0x08048b06      0f85c9000000   jne 0x8048bd5
│       │   0x08048b0c      83ec0c         sub esp, 0xc
│       │   0x08048b0f      ff750c         push dword [s1]             ; const char *s1
│       │   0x08048b12      e80981d4ef     call strlen                 ;[2]; RELOC 32 strlen
│       │   0x08048b17      83c410         add esp, 0x10
│       │   0x08048b1a      83c001         add eax, 1
│       │   0x08048b1d      83ec0c         sub esp, 0xc
│       │   0x08048b20      50             push eax                    ; const char *s1
│       │   0x08048b21      e81aced3ef     call malloc
```

In the code above we can see that it calls `strlen()` and passes `s1` as argument (i.e. `push dword [s1]`).

This means in `eax` we will have the length of `s1`. It then adds `1` to it and passes this value to `malloc()`.

Again, the return of `malloc()` will be in `eax`. So `eax` in this case will be pointing to an allocated memory of size `strlen(s1) + 1`.

Next, it saves the address of the newly allocated memory in a local variable `var_14h`:

```assembly
│       │   0x08048b21      e81aced3ef     call malloc
│       │   0x08048b26      83c410         add esp, 0x10
│       │   0x08048b29      8945ec         mov dword [var_14h], eax
│       │   0x08048b2c      c745f4000000.  mov dword [var_ch], 0
│      ┌──< 0x08048b33      eb1c           jmp 0x8048b51
```

It then proceeds into a loop of size `strlen(s1)`:

> I've renamed 2 local variables for clarity: 
> - `output_buf`: former `var_14h`
> - `count`: former `var_ch`

```assembly
│     ┌───> 0x08048b35      8b55f4         mov edx, dword [count]
│     ╎││   0x08048b38      8b45ec         mov eax, dword [output_buf]
│     ╎││   0x08048b3b      01d0           add eax, edx
│     ╎││   0x08048b3d      8b4df4         mov ecx, dword [count]
│     ╎││   0x08048b40      8b550c         mov edx, dword [s1]
│     ╎││   0x08048b43      01ca           add edx, ecx
│     ╎││   0x08048b45      0fb612         movzx edx, byte [edx]
│     ╎││   0x08048b48      83f20a         xor edx, 0xa
│     ╎││   0x08048b4b      8810           mov byte [eax], dl
│     ╎││   0x08048b4d      8345f401       add dword [count], 1
│     ╎└──> 0x08048b51      83ec0c         sub esp, 0xc
│     ╎ │   0x08048b54      ff750c         push dword [s1]             ; const char *s1
│     ╎ │   0x08048b57      e8c490dbef     call strlen                 ;[2]; RELOC 32 strlen
│     ╎ │   0x08048b5c      83c410         add esp, 0x10
│     ╎ │   0x08048b5f      89c2           mov edx, eax
│     ╎ │   0x08048b61      8b45f4         mov eax, dword [count]
│     ╎ │   0x08048b64      39c2           cmp edx, eax
│     └───< 0x08048b66      77cd           ja 0x8048b35
```

Quick overview of what the loop is doing:

1. Gets char from `s1` (indexed by `count`)
2. Performs a XOR operation between the char from `s1` and a hardcoded value of `0xa`
3. The result of the XOR is stored in the `output_buf`
4. Repeat `strlen(s1)` times

So it seems like we have an encoded password passed to `strncmp()` in the `s1` argument. Let's take a look:

```
:> px 22 @ 0xffe8b6ac
- offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0xffe8b6ac  7365 7f64 6f7c 6f78 6d65 6364 6d7e 656c  se.do|oxmecdm~el
0xffe8b6bc  6364 6e67 6f00                           cdngo.
```

And from the loop above we know that for each byte it performed a `XOR 0xa`, resulting in:

```
:> px 22 @ 0x090a09c0
- offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x090a09c0  796f 756e 6576 6572 676f 696e 6774 6f66  younevergoingtof
0x090a09d0  696e 646d 6500                           indme.
```

And the flag popped out!