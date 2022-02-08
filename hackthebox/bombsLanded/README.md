> source: [https://app.hackthebox.com/challenges/bombs-landed](https://app.hackthebox.com/challenges/bombs-landed)

# Files

Input:
- [BombsLanded](BombsLanded) - Original binary to crack
- [patched_BombsLanded](patched_BombsLanded) - Patched binary

Output:
- [main.md](main.md) - Full disassembly of the `main()` function

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

For the sake of time I won't go over the entire investigation but after some investigation I found this piece of code:

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

It's calling the syscall `ptrace()` and comparing the returned value with `0xffffffff` (which actually means `-1`).

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

After that I decided to patch the binary specially knowing already which execution flow I wanted to explore from the `main()` function.

The `main()` went from this:

<pre>
│           0x080489b6      8b00           mov eax, dword [eax]        ; oeax
│           0x080489b8      39c1           cmp ecx, eax                ; edi ; edi
<mark>│       ┌─< 0x080489ba      7705           ja 0x80489c1</mark>
│       │   0x080489bc      833a04         cmp dword [edx], 4          ; edi ; edi
<mark>│      ┌──< 0x080489bf      7f57           jg 0x8048a18</mark>
│      ││   ; CODE XREF from main @ 0x80489ba
│      │└─> 0x080489c1      833a03         cmp dword [edx], 3          ; edi
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

So with these changes in place we removed all the protections in place.

## Reading the password



# WIP Notes

Important code found in:
jg 0x8048a18

Then enters this call:
```
0x08048aba      ffd0           call eax
```

Then it will ask for the password:


Then we should enter this strcmp call:
```
0xf7f17107      b8e78a0408     mov eax, sym.strncmp
```

Inside this call there will be a loop of 0x10 and the password will be created there, using var_14h as pointer.

```
:> px @ ebp - 0x14
- offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0xffe1e8d4  c099 2908

:> ps @ 0x082999c0
younevergoingtofindme
```