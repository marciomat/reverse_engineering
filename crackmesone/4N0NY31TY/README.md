
> source: https://crackmes.one/crackme/611e76ec33c5d45db85dc2d1

# Tools used

- radare2

# Solution

We first open the binary in radare2 and analyze the binary:

`r2 -A crackme`

By listing the functions we see the `main` and we go directly there:

`s main`

By looking at the disassembly we can right away identify where the _license_ is stored:

```
0x000012e6      488d3d440d00.  lea rdi, str.Enter_License:_
0x000012ed      e8f7feffff     call sym.input
0x000012f2      488945f8       mov qword [var_8h], rax   
```

> Obs: sym.input is not a syscall. It's a normal function where it prints the "Enter License:" string, do a malloc for the user's input and return the address of the input in `rax`

So now we can rename `var_8h` as `input_license`:

`afvn input_license var_8h`

---

Next we find a `for loop` going through each char of the input license:

> I've renamed some local variables to make it easier to understand

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
│      ╎    0x00001324      4889c7         mov rdi, rax                ; int64_t arg1                                                                                                                                                               
│      ╎    0x00001327      e87cffffff     call sym.len                ;[1]                                                                                                                                                                         
│      ╎    0x0000132c      3945f4         cmp dword [i_loop], eax                                                                                                                                                                                  
│      └──< 0x0000132f      7cd5           jl 0x1306                   ; while (i_loop < strlen(input_license)) 
```

