```assembly
            ; DATA XREF from entry0 @ 0x10d1
┌ 180: int main (uint32_t argc, char **argv);
│           ; var char **s @ rbp-0x10
│           ; var uint32_t var_4h @ rbp-0x4
│           ; arg uint32_t argc @ rdi
│           ; arg char **argv @ rsi
│           0x000013db      55             push rbp
│           0x000013dc      4889e5         mov rbp, rsp
│           0x000013df      4883ec10       sub rsp, 0x10
│           0x000013e3      897dfc         mov dword [var_4h], edi     ; argc
│           0x000013e6      488975f0       mov qword [s], rsi          ; argv
│           0x000013ea      837dfc01       cmp dword [var_4h], 1
│       ┌─< 0x000013ee      7519           jne 0x1409
│       │   0x000013f0      488b45f0       mov rax, qword [s]
│       │   0x000013f4      488b00         mov rax, qword [rax]
│       │   0x000013f7      4889c7         mov rdi, rax                ; int64_t arg1
│       │   0x000013fa      e8aafdffff     call sym._9ff8a42e_cbd2_481f_9c73_6880f720771f
│       │   0x000013ff      b801000000     mov eax, 1
│      ┌──< 0x00001404      e984000000     jmp 0x148d
│      ││   ; CODE XREF from main @ 0x13ee
│      │└─> 0x00001409      488b45f0       mov rax, qword [s]
│      │    0x0000140d      4883c008       add rax, 8
│      │    0x00001411      488b00         mov rax, qword [rax]
│      │    0x00001414      4889c7         mov rdi, rax                ; const char *s
│      │    0x00001417      e844fcffff     call sym.imp.strlen         ; size_t strlen(const char *s)
│      │    0x0000141c      83e001         and eax, 1
│      │    0x0000141f      4885c0         test rax, rax
│      │┌─< 0x00001422      7416           je 0x143a
│      ││   0x00001424      488d05350c00.  lea rax, obj._dbf69e5f_8300_41c9_8c80_02a819c56349 ; 0x2060
│      ││   0x0000142b      4889c7         mov rdi, rax                ; char *arg1
│      ││   0x0000142e      e83dfeffff     call sym._a97962fc_d68f_47c5_9221_d17da57166a4
│      ││   0x00001433      b801000000     mov eax, 1
│     ┌───< 0x00001438      eb53           jmp 0x148d
│     │││   ; CODE XREF from main @ 0x1422
│     ││└─> 0x0000143a      488b45f0       mov rax, qword [s]
│     ││    0x0000143e      4883c008       add rax, 8
│     ││    0x00001442      488b00         mov rax, qword [rax]
│     ││    0x00001445      4889c7         mov rdi, rax                ; int64_t arg1
│     ││    0x00001448      e8d4feffff     call sym._99adb5ad_c9d1_44ff_84ce_b52782ac7aeb
│     ││    0x0000144d      4889c6         mov rsi, rax                ; const char *s2
│     ││    0x00001450      488d05c90b00.  lea rax, obj._867a0be1_691e_4546_9b6c_020df3bcdc93 ; 0x2020 ; "]\x10\x14LC\x10CNM\x14?GL4#&A[(R\x10\x11?S\x11LTR"
│     ││    0x00001457      4889c7         mov rdi, rax                ; const char *s1
│     ││    0x0000145a      e831fcffff     call sym.imp.strcmp         ; int strcmp(const char *s1, const char *s2)
│     ││    0x0000145f      85c0           test eax, eax
│     ││┌─< 0x00001461      7416           je 0x1479
│     │││   0x00001463      488d05f60b00.  lea rax, obj._dbf69e5f_8300_41c9_8c80_02a819c56349 ; 0x2060
│     │││   0x0000146a      4889c7         mov rdi, rax                ; char *arg1
│     │││   0x0000146d      e8fefdffff     call sym._a97962fc_d68f_47c5_9221_d17da57166a4
│     │││   0x00001472      b801000000     mov eax, 1
│    ┌────< 0x00001477      eb14           jmp 0x148d
│    ││││   ; CODE XREF from main @ 0x1461
│    │││└─> 0x00001479      488d05000c00.  lea rax, obj._a67bcbe1_4a3e_4c27_a894_ae121b083cac ; 0x2080
│    │││    0x00001480      4889c7         mov rdi, rax                ; char *arg1
│    │││    0x00001483      e8e8fdffff     call sym._a97962fc_d68f_47c5_9221_d17da57166a4
│    │││    0x00001488      b800000000     mov eax, 0
│    │││    ; CODE XREFS from main @ 0x1404, 0x1438, 0x1477
│    └└└──> 0x0000148d      c9             leave
└           0x0000148e      c3             ret
```
