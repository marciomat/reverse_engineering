```assembly
            ; DATA XREF from entry0 @ 0x1121
┌ 145: int main (int argc, char **argv, char **envp);
│           ; var uint32_t var_10h @ rbp-0x10
│           ; var signed int64_t var_ch @ rbp-0xc
│           ; var int64_t var_8h @ rbp-0x8
│           0x000012da      f30f1efa       endbr64
│           0x000012de      55             push rbp
│           0x000012df      4889e5         mov rbp, rsp
│           0x000012e2      4883ec10       sub rsp, 0x10
│           0x000012e6      488d3d440d00.  lea rdi, str.Enter_License:_ ; 0x2031 ; "Enter License: " ; int64_t arg1
│           0x000012ed      e8f7feffff     call sym.input
│           0x000012f2      488945f8       mov qword [var_8h], rax
│           0x000012f6      c745f0000000.  mov dword [var_10h], 0
│           0x000012fd      c745f4000000.  mov dword [var_ch], 0
│       ┌─< 0x00001304      eb1a           jmp 0x1320
│       │   ; CODE XREF from main @ 0x132f
│      ┌──> 0x00001306      8b45f4         mov eax, dword [var_ch]
│      ╎│   0x00001309      4863d0         movsxd rdx, eax
│      ╎│   0x0000130c      488b45f8       mov rax, qword [var_8h]
│      ╎│   0x00001310      4801d0         add rax, rdx
│      ╎│   0x00001313      0fb600         movzx eax, byte [rax]
│      ╎│   0x00001316      0fbec0         movsx eax, al
│      ╎│   0x00001319      0145f0         add dword [var_10h], eax
│      ╎│   0x0000131c      8345f401       add dword [var_ch], 1
│      ╎│   ; CODE XREF from main @ 0x1304
│      ╎└─> 0x00001320      488b45f8       mov rax, qword [var_8h]
│      ╎    0x00001324      4889c7         mov rdi, rax                ; int64_t arg1
│      ╎    0x00001327      e87cffffff     call sym.len
│      ╎    0x0000132c      3945f4         cmp dword [var_ch], eax
│      └──< 0x0000132f      7cd5           jl 0x1306
│           0x00001331      488b45f8       mov rax, qword [var_8h]
│           0x00001335      4889c7         mov rdi, rax                ; int64_t arg1
│           0x00001338      e86bffffff     call sym.len
│           0x0000133d      6bc0f6         imul eax, eax, 0xfffffff6
│           0x00001340      05e7340000     add eax, 0x34e7
│           0x00001345      3945f0         cmp dword [var_10h], eax
│       ┌─< 0x00001348      750e           jne 0x1358
│       │   0x0000134a      488d3df00c00.  lea rdi, str._nLicense_is_valid_ ; 0x2041 ; "\nLicense is valid!" ; const char *s
│       │   0x00001351      e84afdffff     call sym.imp.puts           ; int puts(const char *s)
│      ┌──< 0x00001356      eb0c           jmp 0x1364
│      ││   ; CODE XREF from main @ 0x1348
│      │└─> 0x00001358      488d3df50c00.  lea rdi, str._nInvalid_license_ ; 0x2054 ; "\nInvalid license!" ; const char *s
│      │    0x0000135f      e83cfdffff     call sym.imp.puts           ; int puts(const char *s)
│      │    ; CODE XREF from main @ 0x1356
│      └──> 0x00001364      b800000000     mov eax, 0
│           0x00001369      c9             leave
└           0x0000136a      c3             ret
```
