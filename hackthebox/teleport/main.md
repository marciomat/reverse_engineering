```assembly
            ; DATA XREF from entry0 @ 0xa3d
┌ 245: int main (uint32_t argc, char **argv);
│           ; var char **src @ rbp-0x20
│           ; var uint32_t var_14h @ rbp-0x14
│           ; var int64_t var_8h @ rbp-0x8
│           ; var int64_t var_4h @ rbp-0x4
│           ; arg uint32_t argc @ rdi
│           ; arg char **argv @ rsi
│           0x00001696      55             push rbp
│           0x00001697      4889e5         mov rbp, rsp
│           0x0000169a      4883ec20       sub rsp, 0x20
│           0x0000169e      897dec         mov dword [var_14h], edi    ; argc
│           0x000016a1      488975e0       mov qword [src], rsi        ; argv
│           0x000016a5      837dec02       cmp dword [var_14h], 2
│       ┌─< 0x000016a9      7416           je 0x16c1
│       │   0x000016ab      488d3d620100.  lea rdi, str.Missing_password ; 0x1814 ; "Missing password" ; const char *s
│       │   0x000016b2      e829f3ffff     call sym.imp.puts           ; int puts(const char *s)
│       │   0x000016b7      b8ffffffff     mov eax, 0xffffffff         ; -1
│      ┌──< 0x000016bc      e9c8000000     jmp 0x1789
│      ││   ; CODE XREF from main @ 0x16a9
│      │└─> 0x000016c1      488b45e0       mov rax, qword [src]
│      │    0x000016c5      4883c008       add rax, 8
│      │    0x000016c9      488b00         mov rax, qword [rax]
│      │    0x000016cc      ba64000000     mov edx, 0x64               ; 'd' ; size_t  n
│      │    0x000016d1      4889c6         mov rsi, rax                ; const char *src
│      │    0x000016d4      488d3da51b20.  lea rdi, [0x00203280]       ; char *dest
│      │    0x000016db      e8f0f2ffff     call sym.imp.strncpy        ; char *strncpy(char *dest, const char *src, size_t  n)
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
│      │    0x00001714      488d3d851a20.  lea rdi, [0x002031a0]       ; jmpbuf env
│      │    0x0000171b      e8d0f2ffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
│      │    0x00001720      8945fc         mov dword [var_4h], eax
│      │    0x00001723      8b45fc         mov eax, dword [var_4h]
│      │    0x00001726      83f864         cmp eax, 0x64
│      │┌─< 0x00001729      7407           je 0x1732
│      ││   0x0000172b      83f865         cmp eax, 0x65
│     ┌───< 0x0000172e      7410           je 0x1740
│    ┌────< 0x00001730      eb1c           jmp 0x174e
│    ││││   ; CODE XREF from main @ 0x1729
│    │││└─> 0x00001732      488d3dec0000.  lea rdi, str.Looks_good_to_me_ ; 0x1825 ; "Looks good to me!" ; const char *s
│    │││    0x00001739      e8a2f2ffff     call sym.imp.puts           ; int puts(const char *s)
│    │││┌─< 0x0000173e      eb44           jmp 0x1784
│    ││││   ; CODE XREF from main @ 0x172e
│    │└───> 0x00001740      488d3df00000.  lea rdi, str.Somethings_wrong... ; 0x1837 ; "Something's wrong..." ; const char *s
│    │ ││   0x00001747      e894f2ffff     call sym.imp.puts           ; int puts(const char *s)
│    │┌───< 0x0000174c      eb36           jmp 0x1784
│    ││││   ; CODE XREF from main @ 0x1730
│    └────> 0x0000174e      8b45fc         mov eax, dword [var_4h]
│     │││   0x00001751      4863d0         movsxd rdx, eax
│     │││   0x00001754      4889d0         mov rax, rdx
│     │││   0x00001757      48c1e002       shl rax, 2
│     │││   0x0000175b      4801d0         add rax, rdx
│     │││   0x0000175e      488d14850000.  lea rdx, [rax*4]
│     │││   0x00001766      4801d0         add rax, rdx
│     │││   0x00001769      48c1e003       shl rax, 3
│     │││   0x0000176d      488d158c1b20.  lea rdx, [0x00203300]
│     │││   0x00001774      4801d0         add rax, rdx
│     │││   0x00001777      be01000000     mov esi, 1                  ; int val
│     │││   0x0000177c      4889c7         mov rdi, rax                ; jmp_buf env
│     │││   0x0000177f      e87cf2ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
│     │││   ; CODE XREFS from main @ 0x173e, 0x174c
│     └─└─> 0x00001784      b800000000     mov eax, 0
│      │    ; CODE XREF from main @ 0x16bc
│      └──> 0x00001789      c9             leave
└           0x0000178a      c3             ret
```
