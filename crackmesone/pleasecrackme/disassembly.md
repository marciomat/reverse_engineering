```assembly
            ; DATA XREF from entry0 @ 0x1121
┌ 355: int main (int argc, char **argv, char **envp);
│           ; var int64_t var_78h @ rbp-0x78
│           ; var int64_t var_74h @ rbp-0x74
│           ; var char *s @ rbp-0x70
│           ; var char *s1 @ rbp-0x50
│           ; var char *s2 @ rbp-0x30
│           ; var int64_t canary @ rbp-0x18
│           0x000011e9      f30f1efa       endbr64
│           0x000011ed      55             push rbp
│           0x000011ee      4889e5         mov rbp, rsp
│           0x000011f1      53             push rbx
│           0x000011f2      4883ec78       sub rsp, 0x78
│           0x000011f6      64488b042528.  mov rax, qword fs:[0x28]
│           0x000011ff      488945e8       mov qword [canary], rax
│           0x00001203      31c0           xor eax, eax
│           0x00001205      488d3dfc0d00.  lea rdi, str.Type_in_your_Username:_ ; 0x2008 ; "Type in your Username: " ; const char *format
│           0x0000120c      b800000000     mov eax, 0
│           0x00001211      e8bafeffff     call sym.imp.printf         ; int printf(const char *format)
│           0x00001216      488d4590       lea rax, [s]
│           0x0000121a      4889c6         mov rsi, rax
│           0x0000121d      488d3dfc0d00.  lea rdi, [0x00002020]       ; "%s" ; const char *format
│           0x00001224      b800000000     mov eax, 0
│           0x00001229      e8c2feffff     call sym.imp.__isoc99_scanf ; int scanf(const char *format)
│           0x0000122e      488d3df30d00.  lea rdi, str._nType_in_a_number_beetween_1_and_9:_ ; 0x2028 ; "\nType in a number beetween 1 and 9: " ; const char *format
│           0x00001235      b800000000     mov eax, 0
│           0x0000123a      e891feffff     call sym.imp.printf         ; int printf(const char *format)
│           0x0000123f      488d4588       lea rax, [var_78h]
│           0x00001243      4889c6         mov rsi, rax
│           0x00001246      488d3d000e00.  lea rdi, [0x0000204d]       ; "%d" ; const char *format
│           0x0000124d      b800000000     mov eax, 0
│           0x00001252      e899feffff     call sym.imp.__isoc99_scanf ; int scanf(const char *format)
│           0x00001257      8b4588         mov eax, dword [var_78h]
│           0x0000125a      85c0           test eax, eax
│       ┌─< 0x0000125c      7f16           jg 0x1274
│       │   0x0000125e      488d3deb0d00.  lea rdi, str._nError:_Number_is_too_small ; 0x2050 ; "\nError: Number is too small" ; const char *s
│       │   0x00001265      e836feffff     call sym.imp.puts           ; int puts(const char *s)
│       │   0x0000126a      b8ffffffff     mov eax, 0xffffffff         ; -1
│      ┌──< 0x0000126f      e9bd000000     jmp 0x1331
│      ││   ; CODE XREF from main @ 0x125c
│      │└─> 0x00001274      8b4588         mov eax, dword [var_78h]
│      │    0x00001277      83f809         cmp eax, 9
│      │┌─< 0x0000127a      7e16           jle 0x1292
│      ││   0x0000127c      488d3de90d00.  lea rdi, str._nError:_Number_is_too_big ; 0x206c ; "\nError: Number is too big" ; const char *s
│      ││   0x00001283      e818feffff     call sym.imp.puts           ; int puts(const char *s)
│      ││   0x00001288      b8ffffffff     mov eax, 0xffffffff         ; -1
│     ┌───< 0x0000128d      e99f000000     jmp 0x1331
│     │││   ; CODE XREF from main @ 0x127a
│     ││└─> 0x00001292      c7458c000000.  mov dword [var_74h], 0
│     ││┌─< 0x00001299      eb20           jmp 0x12bb
│     │││   ; CODE XREF from main @ 0x12d0
│    ┌────> 0x0000129b      8b458c         mov eax, dword [var_74h]
│    ╎│││   0x0000129e      4898           cdqe
│    ╎│││   0x000012a0      0fb6440590     movzx eax, byte [rbp + rax - 0x70]
│    ╎│││   0x000012a5      89c2           mov edx, eax
│    ╎│││   0x000012a7      8b4588         mov eax, dword [var_78h]
│    ╎│││   0x000012aa      01d0           add eax, edx
│    ╎│││   0x000012ac      89c2           mov edx, eax
│    ╎│││   0x000012ae      8b458c         mov eax, dword [var_74h]
│    ╎│││   0x000012b1      4898           cdqe
│    ╎│││   0x000012b3      885405b0       mov byte [rbp + rax - 0x50], dl
│    ╎│││   0x000012b7      83458c01       add dword [var_74h], 1
│    ╎│││   ; CODE XREF from main @ 0x1299
│    ╎││└─> 0x000012bb      8b458c         mov eax, dword [var_74h]
│    ╎││    0x000012be      4863d8         movsxd rbx, eax
│    ╎││    0x000012c1      488d4590       lea rax, [s]
│    ╎││    0x000012c5      4889c7         mov rdi, rax                ; const char *s
│    ╎││    0x000012c8      e8e3fdffff     call sym.imp.strlen         ; size_t strlen(const char *s)
│    ╎││    0x000012cd      4839c3         cmp rbx, rax
│    └────< 0x000012d0      72c9           jb 0x129b
│     ││    0x000012d2      488d3dad0d00.  lea rdi, str._nType_in_the_password:_ ; 0x2086 ; "\nType in the password: " ; const char *format
│     ││    0x000012d9      b800000000     mov eax, 0
│     ││    0x000012de      e8edfdffff     call sym.imp.printf         ; int printf(const char *format)
│     ││    0x000012e3      488d45d0       lea rax, [s2]
│     ││    0x000012e7      4889c6         mov rsi, rax
│     ││    0x000012ea      488d3d2f0d00.  lea rdi, [0x00002020]       ; "%s" ; const char *format
│     ││    0x000012f1      b800000000     mov eax, 0
│     ││    0x000012f6      e8f5fdffff     call sym.imp.__isoc99_scanf ; int scanf(const char *format)
│     ││    0x000012fb      488d55d0       lea rdx, [s2]
│     ││    0x000012ff      488d45b0       lea rax, [s1]
│     ││    0x00001303      4889d6         mov rsi, rdx                ; const char *s2
│     ││    0x00001306      4889c7         mov rdi, rax                ; const char *s1
│     ││    0x00001309      e8d2fdffff     call sym.imp.strcmp         ; int strcmp(const char *s1, const char *s2)
│     ││    0x0000130e      85c0           test eax, eax
│     ││┌─< 0x00001310      750e           jne 0x1320
│     │││   0x00001312      488d3d870d00.  lea rdi, str._nYou_are_succesfully_logged_in ; 0x20a0 ; "\nYou are succesfully logged in" ; const char *s
│     │││   0x00001319      e882fdffff     call sym.imp.puts           ; int puts(const char *s)
│    ┌────< 0x0000131e      eb0c           jmp 0x132c
│    ││││   ; CODE XREF from main @ 0x1310
│    │││└─> 0x00001320      488d3d980d00.  lea rdi, str._nWrong_password ; 0x20bf ; "\nWrong password" ; const char *s
│    │││    0x00001327      e874fdffff     call sym.imp.puts           ; int puts(const char *s)
│    │││    ; CODE XREF from main @ 0x131e
│    └────> 0x0000132c      b800000000     mov eax, 0
│     ││    ; CODE XREFS from main @ 0x126f, 0x128d
│     └└──> 0x00001331      488b4de8       mov rcx, qword [canary]
│           0x00001335      6448330c2528.  xor rcx, qword fs:[0x28]
│       ┌─< 0x0000133e      7405           je 0x1345
│       │   0x00001340      e87bfdffff     call sym.imp.__stack_chk_fail ; void __stack_chk_fail(void)
│       │   ; CODE XREF from main @ 0x133e
│       └─> 0x00001345      4883c478       add rsp, 0x78
│           0x00001349      5b             pop rbx
│           0x0000134a      5d             pop rbp
└           0x0000134b      c3             ret
```
