
> source: https://crackmes.one/crackme/611e76ec33c5d45db85dc2d1

# Tools used

- radare2

# Files

Input:
- [611e76ec33c5d45db85dc2d1.zip](611e76ec33c5d45db85dc2d1.zip) - Original crackmesone file
- [crackme](crackme) - Binary to crack

Output:
- [script_crack.py](script_crack.py) - Script created to find the answer

# Solution

We first open the binary in radare2 and analyze the binary:

`r2 -A crackme`

By listing the functions we see the `main()` and we go directly there:

`s main`

By looking at the disassembly we can right away identify where the _license_ is stored:

```
0x000012e6      488d3d440d00.  lea rdi, str.Enter_License:_
0x000012ed      e8f7feffff     call sym.input
0x000012f2      488945f8       mov qword [var_8h], rax   
```

> Obs: sym.input is not a syscall. It's a normal function where it prints the "_Enter License:_" string, do a malloc for the user's input and return the address of the input in `rax`

So now we can rename `var_8h` as `input_license`:

`afvn input_license var_8h`

---

Next we find a `for loop` going through each char of the input license:

> I've renamed some local variables and added comments to make it easier to understand

```
│           0x000012f6      c745f0000000.  mov dword [sum_chars], 0                                                                                                                                                                                 
│           0x000012fd      c745f4000000.  mov dword [i_loop], 0                                                                                                                                                                                    
│       ┌─< 0x00001304      eb1a           jmp 0x1320                                                                                                                                                                                               
│       │   ; CODE XREF from main @ 0x132f                                                                                                                                                                                                          
│      ┌──> 0x00001306      8b45f4         mov eax, dword [i_loop]                                                                                                                                                                                  
│      ╎│   0x00001309      4863d0         movsxd rdx, eax                                                                                                                                                                                          
│      ╎│   0x0000130c      488b45f8       mov rax, qword [input_license]    ; RAX = &input_license                                                                                                                                                 
│      ╎│   0x00001310      4801d0         add rax, rdx                ; increment RAX pointer by 'i_loop'                                                                                                                                          
│      ╎│   0x00001313      0fb600         movzx eax, byte [rax]       ; reads char from indexed position                                                                                                                                           
│      ╎│   0x00001316      0fbec0         movsx eax, al                                                                                                                                                                                            
│      ╎│   0x00001319      0145f0         add dword [sum_chars], eax    ; accumulates the sum of each ASCII char                                                                                                                                   
│      ╎│   0x0000131c      8345f401       add dword [i_loop], 1                                                                                                                                                                                    
│      ╎│   ; CODE XREF from main @ 0x1304                                                                                                                                                                                                          
│      ╎└─> 0x00001320      488b45f8       mov rax, qword [input_license]                                                                                                                                                                           
│      ╎    0x00001324      4889c7         mov rdi, rax
│      ╎    0x00001327      e87cffffff     call sym.len
│      ╎    0x0000132c      3945f4         cmp dword [i_loop], eax                                                                                                                                                                                  
│      └──< 0x0000132f      7cd5           jl 0x1306                   ; while (i_loop < strlen(input_license)) 
```

---

In the following section we have:

```
│           0x00001331      488b45f8       mov rax, qword [input_license]                                                                                                                                                                           
│           0x00001335      4889c7         mov rdi, rax
│           0x00001338      e86bffffff     call sym.len
│           0x0000133d      6bc0f6         imul eax, eax, 0xfffffff6    ; multiply by -10                                                                                                                                                           
│           0x00001340      05e7340000     add eax, 0x34e7                                                                                                                                                                                          
│           0x00001345      3945f0         cmp dword [sum_chars], eax                                                                                                                                                                               
│       ┌─< 0x00001348      750e           jne 0x1358  
```

The above code bascially takes the `strlen(input_license)`, multiplies by (-10) and adds `0x34e7`. The result it compares with `sum_chars` (which is the result of the previous loop).

If the comparison is equal we got a valid license, otherwise it's invalid.

---

Now this is a typical case where a script is the best way to find the correct string. And it's safe to assume that there are multiple answers that would be accepted by the validation check.

The [script](script_crack.py) is very simple.

And by running it, we found the following string as one of the possible answers:

```
ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ!
```
> It consists of 135 `Z` chars followed by `!`
