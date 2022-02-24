```assembly
            ; DATA XREF from main @ 0x564966c066f7
            0x564966c05960      55             push rbp
            0x564966c05961      4157           push r15
            0x564966c05963      4156           push r14
            0x564966c05965      4155           push r13
            0x564966c05967      4154           push r12
            0x564966c05969      53             push rbx
            0x564966c0596a      4881ecf80000.  sub rsp, 0xf8
            0x564966c05971      488d9c248000.  lea rbx, [rsp + 0x80]
            0x564966c05979      4889df         mov rdi, rbx
            0x564966c0597c      ff15f6532400   call qword [0x564966e4ad78] ; [0x564966e4ad78:8]=0x564966c1f000
            0x564966c05982      0f1084248000.  movups xmm0, xmmword [rsp + 0x80]
            0x564966c0598a      0f108c249000.  movups xmm1, xmmword [rsp + 0x90]
            0x564966c05992      0f294c2410     movaps xmmword [rsp + 0x10], xmm1
            0x564966c05997      0f290424       movaps xmmword [rsp], xmm0
            0x564966c0599b      488dbc24a000.  lea rdi, [rsp + 0xa0]
            0x564966c059a3 b    4889e6         mov rsi, rsp
            0x564966c059a6      e855100000     call fcn.00006a00
            0x564966c059ab      488b8424b000.  mov rax, qword [rsp + 0xb0]
            0x564966c059b3      4883f802       cmp rax, 2              ; 2
        ┌─< 0x564966c059b7      0f8591000000   jne 0x564966c05a4e
        │   0x564966c059bd      488b8424a000.  mov rax, qword [rsp + 0xa0]
        │   ;-- rip:
        │   0x564966c059c5 b    4883782829     cmp qword [rax + 0x28], 0x29 ; Compare password lenght with 41 (0x29)
       ┌──< 0x564966c059ca      0f8599000000   jne 0x564966c05a69
       ││   0x564966c059d0      488b5818       mov rbx, qword [rax + 0x18]
       ││   0x564966c059d4      488d059d4303.  lea rax, [0x564966c39d78]
       ││   0x564966c059db      4839c3         cmp rbx, rax
      ┌───< 0x564966c059de      7413           je 0x564966c059f3
      │││   0x564966c059e0      48b87069636f.  movabs rax, 0x7b4654436f636970 ; 'picoCTF{'
      │││   0x564966c059ea      483903         cmp qword [rbx], rax
     ┌────< 0x564966c059ed      0f85e0000000   jne 0x564966c05ad3
     ││││   ; CODE XREF from rip @ +0x19
     │└───> 0x564966c059f3      488d4328       lea rax, [rbx + 0x28]
     │ ││   0x564966c059f7      488d0d964303.  lea rcx, [0x564966c39d94]
     │ ││   0x564966c059fe      4839c8         cmp rax, rcx
     │┌───< 0x564966c05a01      7409           je 0x564966c05a0c
     ││││   0x564966c05a03      80387d         cmp byte [rax], 0x7d    ; compares last char with '}'
    ┌─────< 0x564966c05a06      0f85c7000000   jne 0x564966c05ad3
    │││││   ; CODE XREF from rip @ +0x3c
    ││└───> 0x564966c05a0c      807b08bf       cmp byte [rbx + 8], 0xbf
    ││┌───< 0x564966c05a10      0f8ec4000000   jle 0x564966c05ada
    │││││   0x564966c05a16      4883c308       add rbx, 8
    │││││   0x564966c05a1a      8038bf         cmp byte [rax], 0xbf
   ┌──────< 0x564966c05a1d      0f8ed8000000   jle 0x564966c05afb
   ││││││   0x564966c05a23      bf20000000     mov edi, 0x20           ; 32
   ││││││   0x564966c05a28      be01000000     mov esi, 1
   ││││││   0x564966c05a2d      ff156d532400   call qword [0x564966e4ada0] ; [0x564966e4ada0:8]=0x564966c06da0
   ││││││   0x564966c05a33      4885c0         test rax, rax
  ┌───────< 0x564966c05a36      0f85dd000000   jne 0x564966c05b19
  │││││││   0x564966c05a3c      bf20000000     mov edi, 0x20           ; 32
  │││││││   0x564966c05a41      be01000000     mov esi, 1
  │││││││   0x564966c05a46      ff1574542400   call qword [0x564966e4aec0] ; [0x564966e4aec0:8]=0x564966c32f80
  │││││││   0x564966c05a4c      0f0b           ud2
  │││││││   ; CODE XREF from fcn.00005781 @ +0x236
  ││││││└─> 0x564966c05a4e      4885c0         test rax, rax
  ││││││┌─< 0x564966c05a51      7520           jne 0x564966c05a73
  │││││││   0x564966c05a53      488d15ee2724.  lea rdx, [0x564966e48248]
  │││││││   0x564966c05a5a      31ff           xor edi, edi
  │││││││   0x564966c05a5c      31f6           xor esi, esi
  │││││││   0x564966c05a5e      ff15dc502400   call qword [0x564966e4ab40] ; [0x564966e4ab40:8]=0x564966c356a0
  ────────< 0x564966c05a64      e9ae000000     jmp 0x564966c05b17      ; fcn.00006436-0x91f
  │││││││   ; CODE XREF from rip @ +0x5
  │││││└──> 0x564966c05a69      e8920b0000     call fcn.00006600
  │││││┌──< 0x564966c05a6e      e9a4000000     jmp 0x564966c05b17      ; fcn.00006436-0x91f
  │││││││   ; CODE XREF from rip @ +0x8c
  ││││││└─> 0x564966c05a73      488b8424a000.  mov rax, qword [rsp + 0xa0]
  ││││││    0x564966c05a7b      488984248000.  mov qword [rsp + 0x80], rax
  ││││││    0x564966c05a83      488d0536faff.  lea rax, [0x564966c054c0]
  ││││││    0x564966c05a8a      488984248800.  mov qword [rsp + 0x88], rax
  ││││││    0x564966c05a92      488d058f2724.  lea rax, [0x564966e48228]
  ││││││    0x564966c05a99      48890424       mov qword [rsp], rax
  ││││││    0x564966c05a9d      48c744240802.  mov qword [rsp + 8], 2
  ││││││    0x564966c05aa6      48c744241000.  mov qword [rsp + 0x10], 0
  ││││││    0x564966c05aaf      48895c2420     mov qword [rsp + 0x20], rbx
  ││││││    0x564966c05ab4      48c744242801.  mov qword [rsp + 0x28], 1
  ││││││    0x564966c05abd      4889e7         mov rdi, rsp
  ││││││    0x564966c05ac0      ff1512552400   call qword [0x564966e4afd8] ; [0x564966e4afd8:8]=0x564966c083b0
  ││││││    0x564966c05ac6      bf01000000     mov edi, 1
  ││││││    0x564966c05acb      ff1537532400   call qword [0x564966e4ae08] ; [0x564966e4ae08:8]=0x564966c1f1d0
  ││││││    0x564966c05ad1      eb44           jmp 0x564966c05b17      ; fcn.00006436-0x91f
  ││││││    ; CODE XREFS from rip @ +0x28, +0x41
  ││└└────> 0x564966c05ad3      e8780b0000     call fcn.00006650
  ││  ││    0x564966c05ad8      eb3d           jmp 0x564966c05b17      ; fcn.00006436-0x91f
  ││  ││    ; CODE XREF from rip @ +0x4b
  ││  └───> 0x564966c05ada      4c8d057f2724.  lea r8, [0x564966e48260]
  ││   │    0x564966c05ae1      be29000000     mov esi, 0x29           ; ')' ; 41
  ││   │    0x564966c05ae6      ba08000000     mov edx, 8
  ││   │    0x564966c05aeb      b929000000     mov ecx, 0x29           ; ')' ; 41
  ││   │    0x564966c05af0      4889df         mov rdi, rbx
  ││   │    0x564966c05af3      ff15c7502400   call qword [0x564966e4abc0] ; [0x564966e4abc0:8]=0x564966c34220
  ││   │    0x564966c05af9      eb1c           jmp 0x564966c05b17      ; fcn.00006436-0x91f
  ││   │    ; CODE XREF from rip @ +0x58
  │└──────> 0x564966c05afb      4c8d055e2724.  lea r8, [0x564966e48260]
  │    │    0x564966c05b02      be21000000     mov esi, 0x21           ; '!' ; 33
  │    │    0x564966c05b07      b920000000     mov ecx, 0x20           ; 32
  │    │    0x564966c05b0c      4889df         mov rdi, rbx
  │    │    0x564966c05b0f      31d2           xor edx, edx
  │    │    0x564966c05b11      ff15a9502400   call qword [0x564966e4abc0] ; [0x564966e4abc0:8]=0x564966c34220
│ │    │    ; XREFS(40)
│ ─────└──> 0x564966c05b17      0f0b           ud2
  │         ; CODE XREF from rip @ +0x71
  └───────> 0x564966c05b19      4889442468     mov qword [rsp + 0x68], rax
            0x564966c05b1e      0f28052b3a03.  movaps xmm0, xmmword [section..rodata] ; [0x564966c39550:16]=-1 ; " "
            0x564966c05b25      0f11442470     movups xmmword [rsp + 0x70], xmm0
            0x564966c05b2a      488d7c2468     lea rdi, [rsp + 0x68]
            0x564966c05b2f      ba20000000     mov edx, 0x20           ; 32
            0x564966c05b34      31f6           xor esi, esi
            0x564966c05b36      e8e50b0000     call fcn.00006720
            0x564966c05b3b      488b442468     mov rax, qword [rsp + 0x68]
            0x564966c05b40      488b4c2478     mov rcx, qword [rsp + 0x78]
            0x564966c05b45      0f1003         movups xmm0, xmmword [rbx]
            0x564966c05b48      0f104b10       movups xmm1, xmmword [rbx + 0x10]
            0x564966c05b4c      0f114c0810     movups xmmword [rax + rcx + 0x10], xmm1
            0x564966c05b51      0f110408       movups xmmword [rax + rcx], xmm0
            0x564966c05b55      488d5120       lea rdx, [rcx + 0x20]
            0x564966c05b59      4889542478     mov qword [rsp + 0x78], rdx
            0x564966c05b5e      4885c9         test rcx, rcx
            0x564966c05b61      0f856d070000   jne 0x564966c062d4
            0x564966c05b67      0f1000         movups xmm0, xmmword [rax]
            0x564966c05b6a      0f104810       movups xmm1, xmmword [rax + 0x10]
            0x564966c05b6e      0f294c2410     movaps xmmword [rsp + 0x10], xmm1
            0x564966c05b73      0f290424       movaps xmmword [rsp], xmm0
            0x564966c05b77      488dbc24b800.  lea rdi, [rsp + 0xb8]
            0x564966c05b7f      4889e6         mov rsi, rsp
            0x564966c05b82      31d2           xor edx, edx
            0x564966c05b84      e857f9ffff     call fcn.000054e0
            0x564966c05b89      0f108424b800.  movups xmm0, xmmword [rsp + 0xb8]
            0x564966c05b91      0f108c24c800.  movups xmm1, xmmword [rsp + 0xc8]
            0x564966c05b99      0f294c2410     movaps xmmword [rsp + 0x10], xmm1
            0x564966c05b9e      0f290424       movaps xmmword [rsp], xmm0
            0x564966c05ba2      488dbc24d800.  lea rdi, [rsp + 0xd8]
            0x564966c05baa      4889e6         mov rsi, rsp
            0x564966c05bad      ba01000000     mov edx, 1
            0x564966c05bb2      e829f9ffff     call fcn.000054e0
            0x564966c05bb7      0f108424d800.  movups xmm0, xmmword [rsp + 0xd8]
            0x564966c05bbf      0f108c24e800.  movups xmm1, xmmword [rsp + 0xe8]
            0x564966c05bc7      0f294c2410     movaps xmmword [rsp + 0x10], xmm1
            0x564966c05bcc      0f290424       movaps xmmword [rsp], xmm0
            0x564966c05bd0      488dbc248000.  lea rdi, [rsp + 0x80]
            0x564966c05bd8      4889e6         mov rsi, rsp
            0x564966c05bdb      ba02000000     mov edx, 2
            0x564966c05be0      e8fbf8ffff     call fcn.000054e0
            0x564966c05be5      0f1084248000.  movups xmm0, xmmword [rsp + 0x80]
            0x564966c05bed      0f108c249000.  movups xmm1, xmmword [rsp + 0x90]
            0x564966c05bf5      0f294c2410     movaps xmmword [rsp + 0x10], xmm1
            0x564966c05bfa      0f290424       movaps xmmword [rsp], xmm0
            0x564966c05bfe      488d7c2448     lea rdi, [rsp + 0x48]
            0x564966c05c03      4889e6         mov rsi, rsp
            0x564966c05c06      ba03000000     mov edx, 3
            0x564966c05c0b      e8d0f8ffff     call fcn.000054e0
            0x564966c05c10      408a742448     mov sil, byte [rsp + 0x48]
            0x564966c05c15      448a742449     mov r14b, byte [rsp + 0x49]
            0x564966c05c1a      408a6c244a     mov bpl, byte [rsp + 0x4a]
            0x564966c05c1f      8a44244b       mov al, byte [rsp + 0x4b]
            0x564966c05c23      8844243f       mov byte [rsp + 0x3f], al
            0x564966c05c27      8a44244c       mov al, byte [rsp + 0x4c]
            0x564966c05c2b      88442445       mov byte [rsp + 0x45], al
            0x564966c05c2f      8a44244d       mov al, byte [rsp + 0x4d]
            0x564966c05c33      8844243c       mov byte [rsp + 0x3c], al
            0x564966c05c37      8a44244e       mov al, byte [rsp + 0x4e]
            0x564966c05c3b      88442447       mov byte [rsp + 0x47], al
            0x564966c05c3f      8a44244f       mov al, byte [rsp + 0x4f]
            0x564966c05c43      88442438       mov byte [rsp + 0x38], al
            0x564966c05c47      8a442450       mov al, byte [rsp + 0x50]
            0x564966c05c4b      88442441       mov byte [rsp + 0x41], al
            0x564966c05c4f      8a4c2451       mov cl, byte [rsp + 0x51]
            0x564966c05c53      8a442452       mov al, byte [rsp + 0x52]
            0x564966c05c57      88442446       mov byte [rsp + 0x46], al
            0x564966c05c5b      8a442453       mov al, byte [rsp + 0x53]
            0x564966c05c5f      8844243a       mov byte [rsp + 0x3a], al
            0x564966c05c63      448a642454     mov r12b, byte [rsp + 0x54]
            0x564966c05c68      8a442455       mov al, byte [rsp + 0x55]
            0x564966c05c6c      88442443       mov byte [rsp + 0x43], al
            0x564966c05c70      448a4c2456     mov r9b, byte [rsp + 0x56]
            0x564966c05c75      8a442457       mov al, byte [rsp + 0x57]
            0x564966c05c79      88442437       mov byte [rsp + 0x37], al
            0x564966c05c7d      8a442461       mov al, byte [rsp + 0x61]
            0x564966c05c81      880424         mov byte [rsp], al
            0x564966c05c84      8a442458       mov al, byte [rsp + 0x58]
            0x564966c05c88      8844243b       mov byte [rsp + 0x3b], al
            0x564966c05c8c      8a442459       mov al, byte [rsp + 0x59]
            0x564966c05c90      88442442       mov byte [rsp + 0x42], al
            0x564966c05c94      8a44245a       mov al, byte [rsp + 0x5a]
            0x564966c05c98      88442444       mov byte [rsp + 0x44], al
            0x564966c05c9c      448a54245b     mov r10b, byte [rsp + 0x5b]
            0x564966c05ca1      8a44245c       mov al, byte [rsp + 0x5c]
            0x564966c05ca5      8844243e       mov byte [rsp + 0x3e], al
            0x564966c05ca9      8a44245d       mov al, byte [rsp + 0x5d]
            0x564966c05cad      8844243d       mov byte [rsp + 0x3d], al
            0x564966c05cb1      8a44245e       mov al, byte [rsp + 0x5e]
            0x564966c05cb5      88442439       mov byte [rsp + 0x39], al
            0x564966c05cb9      448a44245f     mov r8b, byte [rsp + 0x5f]
            0x564966c05cbe      8a542460       mov dl, byte [rsp + 0x60]
            0x564966c05cc2      448a5c2462     mov r11b, byte [rsp + 0x62]
            0x564966c05cc7      448a7c2463     mov r15b, byte [rsp + 0x63]
            0x564966c05ccc      8a442464       mov al, byte [rsp + 0x64]
            0x564966c05cd0      88442440       mov byte [rsp + 0x40], al
            0x564966c05cd4      8a442465       mov al, byte [rsp + 0x65]
            0x564966c05cd8      8a5c2466       mov bl, byte [rsp + 0x66]
            0x564966c05cdc  ~   885c2436       mov byte [rsp + 0x36], bl
            ; CALL XREF from section..rela.dyn @ +0x2748
│           0x564966c05cde      2436           and al, 0x36            ; 54
│           0x564966c05ce0      448a6c2467     mov r13b, byte [arg_67h]
│           0x564966c05ce5      8a1c24         mov bl, byte [rsp]
│           0x564966c05ce8      48c704241900.  mov qword [rsp], 0x19   ; [0x19:8]=-1 ; 25
│           0x564966c05cf0      488b3c24       mov rdi, qword [rsp]
│           0x564966c05cf4      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c05cf8      0f87e0050000   ja 0x564966c062de
│           0x564966c05cfe      40886c2433     mov byte [arg_33h], bpl
│           0x564966c05d03      88542434       mov byte [arg_34h], dl
│           0x564966c05d07      884c2435       mov byte [arg_35h], cl
│           0x564966c05d0b      488d2d834003.  lea rbp, [0x564966c39d95]
│           0x564966c05d12      3a1c2f         cmp bl, byte [rdi + rbp]
│           0x564966c05d15      0f85da050000   jne 0x564966c062f5      ; check 1
│           0x564966c05d1b      40883424       mov byte [rsp], sil
│           0x564966c05d1f      8a1c24         mov bl, byte [rsp]
│           0x564966c05d22      48c704240000.  mov qword [rsp], 0
│           0x564966c05d2a      488b3c24       mov rdi, qword [rsp]
│           0x564966c05d2e      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c05d32      0f87c7050000   ja 0x564966c062ff
│           0x564966c05d38      488d35564003.  lea rsi, [0x564966c39d95]
│           0x564966c05d3f      3a1c37         cmp bl, byte [rdi + rsi] ; check 2
│           0x564966c05d42      0f85ad050000   jne 0x564966c062f5
│           0x564966c05d48      44880c24       mov byte [rsp], r9b
│           0x564966c05d4c      408a3424       mov sil, byte [rsp]
│           0x564966c05d50      48c704240e00.  mov qword [rsp], 0xe    ; [0xe:8]=-1 ; 14
│           0x564966c05d58      488b3c24       mov rdi, qword [rsp]
│           0x564966c05d5c      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c05d60      0f87b0050000   ja 0x564966c06316
│           0x564966c05d66      488d1d284003.  lea rbx, [0x564966c39d95]
│           0x564966c05d6d      403a341f       cmp sil, byte [rdi + rbx]
│           0x564966c05d71      0f857e050000   jne 0x564966c062f5      ; check 3
│           0x564966c05d77      44881424       mov byte [rsp], r10b
│           0x564966c05d7b      408a3424       mov sil, byte [rsp]
│           0x564966c05d7f      48c704241300.  mov qword [rsp], 0x13   ; [0x13:8]=-1 ; 19
│           0x564966c05d87      488b3c24       mov rdi, qword [rsp]
│           0x564966c05d8b      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c05d8f      0f8798050000   ja 0x564966c0632d
│           0x564966c05d95      488d1df93f03.  lea rbx, [0x564966c39d95]
│           0x564966c05d9c      403a341f       cmp sil, byte [rdi + rbx] ; check 4
│           0x564966c05da0      0f854f050000   jne 0x564966c062f5
│           0x564966c05da6      44880424       mov byte [rsp], r8b
│           0x564966c05daa      408a3424       mov sil, byte [rsp]
│           0x564966c05dae      48c704241700.  mov qword [rsp], 0x17   ; [0x17:8]=-1 ; 23
│           0x564966c05db6      488b3c24       mov rdi, qword [rsp]
│           0x564966c05dba      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c05dbe      0f8780050000   ja 0x564966c06344
│           0x564966c05dc4      488d1dca3f03.  lea rbx, [0x564966c39d95]
│           0x564966c05dcb      403a341f       cmp sil, byte [rdi + rbx]
│           0x564966c05dcf      0f8520050000   jne 0x564966c062f5      ; check 5
│           0x564966c05dd5      44883424       mov byte [rsp], r14b
│           0x564966c05dd9      8a0c24         mov cl, byte [rsp]
│           0x564966c05ddc      48c704240100.  mov qword [rsp], 1
│           0x564966c05de4      488b3c24       mov rdi, qword [rsp]
│           0x564966c05de8      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c05dec      0f8769050000   ja 0x564966c0635b
│           0x564966c05df2      488d359c3f03.  lea rsi, [0x564966c39d95]
│           0x564966c05df9      3a0c37         cmp cl, byte [rdi + rsi]
│           0x564966c05dfc      0f85f3040000   jne 0x564966c062f5      ; check 6
│           0x564966c05e02      880424         mov byte [rsp], al
│           ; DATA XREF from fcn.0004755a @ +0x32f
│           0x564966c05e05      8a0424         mov al, byte [rsp]
│           0x564966c05e08      48c704241d00.  mov qword [rsp], 0x1d   ; [0x1d:8]=-1 ; 29
│           0x564966c05e10      488b3c24       mov rdi, qword [rsp]
│           0x564966c05e14      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c05e18      0f8754050000   ja 0x564966c06372
│           0x564966c05e1e      488d0d703f03.  lea rcx, [0x564966c39d95]
│           0x564966c05e25      3a040f         cmp al, byte [rdi + rcx]
│           0x564966c05e28      0f85c7040000   jne 0x564966c062f5      ; check 7
│           0x564966c05e2e      44883c24       mov byte [rsp], r15b
│           0x564966c05e32      8a0424         mov al, byte [rsp]
│           0x564966c05e35      48c704241b00.  mov qword [rsp], 0x1b   ; [0x1b:8]=-1 ; 27
│           0x564966c05e3d      488b3c24       mov rdi, qword [rsp]
│           0x564966c05e41      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c05e45      0f873e050000   ja 0x564966c06389
│           0x564966c05e4b      488d0d433f03.  lea rcx, [0x564966c39d95]
│           0x564966c05e52      3a040f         cmp al, byte [rdi + rcx]
│           0x564966c05e55      0f859a040000   jne 0x564966c062f5      ; check 8
│           0x564966c05e5b      44881c24       mov byte [rsp], r11b
│           0x564966c05e5f      8a0424         mov al, byte [rsp]
│           0x564966c05e62      48c704241a00.  mov qword [rsp], 0x1a   ; [0x1a:8]=-1 ; 26
│           0x564966c05e6a      488b3c24       mov rdi, qword [rsp]
│           0x564966c05e6e      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c05e72      0f8728050000   ja 0x564966c063a0
│           0x564966c05e78      488d0d163f03.  lea rcx, [0x564966c39d95]
│           0x564966c05e7f      3a040f         cmp al, byte [rdi + rcx]
│           0x564966c05e82      0f856d040000   jne 0x564966c062f5      ; check 9
│           0x564966c05e88      44882424       mov byte [rsp], r12b
│           0x564966c05e8c      8a0424         mov al, byte [rsp]
│           0x564966c05e8f      48c704240c00.  mov qword [rsp], 0xc    ; [0xc:8]=-1 ; 12
│           0x564966c05e97      488b3c24       mov rdi, qword [rsp]
│           0x564966c05e9b      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c05e9f      0f8712050000   ja 0x564966c063b7
│           0x564966c05ea5      488d0de93e03.  lea rcx, [0x564966c39d95]
│           0x564966c05eac      3a040f         cmp al, byte [rdi + rcx]
│           0x564966c05eaf      0f8540040000   jne 0x564966c062f5      ; check 10
│           0x564966c05eb5      44882c24       mov byte [rsp], r13b
│           0x564966c05eb9      8a0424         mov al, byte [rsp]
│           0x564966c05ebc      48c704241f00.  mov qword [rsp], 0x1f   ; [0x1f:8]=-1 ; 31
│           0x564966c05ec4      488b3c24       mov rdi, qword [rsp]
│           0x564966c05ec8      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c05ecc      0f87fc040000   ja 0x564966c063ce
│           0x564966c05ed2      488d0dbc3e03.  lea rcx, [0x564966c39d95]
│           0x564966c05ed9      3a040f         cmp al, byte [rdi + rcx]
│           0x564966c05edc      0f8513040000   jne 0x564966c062f5      ; check 11
│           0x564966c05ee2      8a442447       mov al, byte [arg_47h]
│           0x564966c05ee6      880424         mov byte [rsp], al
│           0x564966c05ee9      8a0424         mov al, byte [rsp]
│           0x564966c05eec      48c704240600.  mov qword [rsp], 6
│           0x564966c05ef4      488b3c24       mov rdi, qword [rsp]
│           0x564966c05ef8      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c05efc      0f87e3040000   ja 0x564966c063e5
│           0x564966c05f02      488d0d8c3e03.  lea rcx, [0x564966c39d95]
│           0x564966c05f09      3a040f         cmp al, byte [rdi + rcx]
│           0x564966c05f0c      0f85e3030000   jne 0x564966c062f5      ; check 12
│           0x564966c05f12      8a442446       mov al, byte [arg_46h]
│           0x564966c05f16      880424         mov byte [rsp], al
│           0x564966c05f19      8a0424         mov al, byte [rsp]
│           0x564966c05f1c      48c704240a00.  mov qword [rsp], 0xa
│           0x564966c05f24      488b3c24       mov rdi, qword [rsp]
│           0x564966c05f28      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c05f2c      0f87ca040000   ja 0x564966c063fc
│           0x564966c05f32      488d0d5c3e03.  lea rcx, [0x564966c39d95]
│           0x564966c05f39      3a040f         cmp al, byte [rdi + rcx]
│           0x564966c05f3c      0f85b3030000   jne 0x564966c062f5      ; check 13
│           0x564966c05f42      8a442437       mov al, byte [arg_37h]
│           0x564966c05f46      880424         mov byte [rsp], al
│           0x564966c05f49      8a0424         mov al, byte [rsp]
│           0x564966c05f4c      48c704240f00.  mov qword [rsp], 0xf    ; [0xf:8]=-1 ; 15
│           0x564966c05f54      488b3c24       mov rdi, qword [rsp]
│           0x564966c05f58      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c05f5c      0f87b1040000   ja 0x564966c06413
│           0x564966c05f62      488d0d2c3e03.  lea rcx, [0x564966c39d95]
│           0x564966c05f69      3a040f         cmp al, byte [rdi + rcx]
│           0x564966c05f6c      0f8583030000   jne 0x564966c062f5      ; check 14
│           0x564966c05f72      8a442436       mov al, byte [arg_36h]
│           0x564966c05f76      880424         mov byte [rsp], al
│           0x564966c05f79      8a0424         mov al, byte [rsp]
│           0x564966c05f7c      48c704241e00.  mov qword [rsp], 0x1e   ; [0x1e:8]=-1 ; 30
│           0x564966c05f84      488b3c24       mov rdi, qword [rsp]
│           0x564966c05f88      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c05f8c      0f8798040000   ja 0x564966c0642a
│           0x564966c05f92      488d0dfc3d03.  lea rcx, [0x564966c39d95]
│           0x564966c05f99      3a040f         cmp al, byte [rdi + rcx]
│           0x564966c05f9c      0f8553030000   jne 0x564966c062f5      ; check 15
│           0x564966c05fa2      8a442438       mov al, byte [arg_38h]
│           0x564966c05fa6      880424         mov byte [rsp], al
│           0x564966c05fa9      8a0424         mov al, byte [rsp]
│           0x564966c05fac      48c704240700.  mov qword [rsp], 7
│           0x564966c05fb4      488b3c24       mov rdi, qword [rsp]
│           0x564966c05fb8      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c05fbc      0f877f040000   ja 0x564966c06441
│           0x564966c05fc2      488d0dcc3d03.  lea rcx, [0x564966c39d95]
│           0x564966c05fc9      3a040f         cmp al, byte [rdi + rcx]
│           0x564966c05fcc      0f8523030000   jne 0x564966c062f5      ; check 16
│           0x564966c05fd2      8a44243a       mov al, byte [arg_3ah]
│           0x564966c05fd6      880424         mov byte [rsp], al
│           0x564966c05fd9      8a0424         mov al, byte [rsp]
│           0x564966c05fdc      48c704240b00.  mov qword [rsp], 0xb    ; [0xb:8]=-1 ; 11
│           0x564966c05fe4      488b3c24       mov rdi, qword [rsp]
│           0x564966c05fe8      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c05fec      0f8766040000   ja 0x564966c06458
│           0x564966c05ff2      488d0d9c3d03.  lea rcx, [0x564966c39d95]
│           0x564966c05ff9      3a040f         cmp al, byte [rdi + rcx]
│           0x564966c05ffc      0f85f3020000   jne 0x564966c062f5      ; check 17
│           0x564966c06002      8a44243c       mov al, byte [arg_3ch]
│           0x564966c06006      880424         mov byte [rsp], al
│           0x564966c06009      8a0424         mov al, byte [rsp]
│           0x564966c0600c      48c704240500.  mov qword [rsp], 5
│           0x564966c06014      488b3c24       mov rdi, qword [rsp]
│           0x564966c06018      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c0601c      0f874d040000   ja 0x564966c0646f
│           0x564966c06022      488d0d6c3d03.  lea rcx, [0x564966c39d95]
│           0x564966c06029      3a040f         cmp al, byte [rdi + rcx]
│           0x564966c0602c      0f85c3020000   jne 0x564966c062f5      ; check 18
│           0x564966c06032      8a442439       mov al, byte [arg_39h]
│           0x564966c06036      880424         mov byte [rsp], al
│           0x564966c06039      8a0424         mov al, byte [rsp]
│           0x564966c0603c      48c704241600.  mov qword [rsp], 0x16   ; [0x16:8]=-1 ; 22
│           0x564966c06044      488b3c24       mov rdi, qword [rsp]
│           0x564966c06048      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c0604c      0f8734040000   ja 0x564966c06486
│           0x564966c06052      488d0d3c3d03.  lea rcx, [0x564966c39d95]
│           0x564966c06059      3a040f         cmp al, byte [rdi + rcx]
│           0x564966c0605c      0f8593020000   jne 0x564966c062f5      ; check 19
│           0x564966c06062      8a44243b       mov al, byte [arg_3bh]
│           0x564966c06066      880424         mov byte [rsp], al
│           0x564966c06069      8a0424         mov al, byte [rsp]
│           0x564966c0606c      48c704241000.  mov qword [rsp], 0x10   ; [0x10:8]=-1 ; 16
│           0x564966c06074      488b3c24       mov rdi, qword [rsp]
│           0x564966c06078      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c0607c      0f871b040000   ja 0x564966c0649d
│           0x564966c06082      488d0d0c3d03.  lea rcx, [0x564966c39d95]
│           0x564966c06089      3a040f         cmp al, byte [rdi + rcx]
│           0x564966c0608c      0f8563020000   jne 0x564966c062f5      ; check 20
│           0x564966c06092      8a44243d       mov al, byte [arg_3dh]
│           0x564966c06096      880424         mov byte [rsp], al
│           0x564966c06099      8a0424         mov al, byte [rsp]
│           ; DATA XREF from fcn.00036010 @ +0x1396
│           0x564966c0609c      48c704241500.  mov qword [rsp], 0x15   ; [0x15:8]=-1 ; 21
│           0x564966c060a4      488b3c24       mov rdi, qword [rsp]
│           0x564966c060a8      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c060ac      0f8702040000   ja 0x564966c064b4
│           0x564966c060b2      488d0ddc3c03.  lea rcx, [0x564966c39d95]
│           0x564966c060b9      3a040f         cmp al, byte [rdi + rcx]
│           0x564966c060bc      0f8533020000   jne 0x564966c062f5      ; check 21
│           0x564966c060c2      8a44243f       mov al, byte [arg_3fh]
│           0x564966c060c6      880424         mov byte [rsp], al
│           0x564966c060c9      8a0424         mov al, byte [rsp]
│           0x564966c060cc      48c704240300.  mov qword [rsp], 3
│           0x564966c060d4      488b3c24       mov rdi, qword [rsp]
│           0x564966c060d8      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c060dc      0f87e9030000   ja 0x564966c064cb
│           0x564966c060e2      488d0dac3c03.  lea rcx, [0x564966c39d95]
│           0x564966c060e9      3a040f         cmp al, byte [rdi + rcx]
│           0x564966c060ec      0f8503020000   jne 0x564966c062f5      ; check 22
│           0x564966c060f2      8a44243e       mov al, byte [arg_3eh]
│           0x564966c060f6      880424         mov byte [rsp], al
│           0x564966c060f9      8a0424         mov al, byte [rsp]
│           0x564966c060fc      48c704241400.  mov qword [rsp], 0x14   ; [0x14:8]=-1 ; 20
│           0x564966c06104      488b3c24       mov rdi, qword [rsp]
│           0x564966c06108      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c0610c      0f87d0030000   ja 0x564966c064e2
│           0x564966c06112      488d0d7c3c03.  lea rcx, [0x564966c39d95]
│           0x564966c06119      3a040f         cmp al, byte [rdi + rcx]
│           0x564966c0611c      0f85d3010000   jne 0x564966c062f5      ; check 23
│           0x564966c06122      8a442441       mov al, byte [arg_41h]
│           0x564966c06126      880424         mov byte [rsp], al
│           0x564966c06129      8a0424         mov al, byte [rsp]
│           0x564966c0612c      48c704240800.  mov qword [rsp], 8
│           0x564966c06134      488b3c24       mov rdi, qword [rsp]
│           0x564966c06138      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c0613c      0f87b7030000   ja 0x564966c064f9
│           0x564966c06142      488d0d4c3c03.  lea rcx, [0x564966c39d95]
│           0x564966c06149      3a040f         cmp al, byte [rdi + rcx]
│           0x564966c0614c      0f85a3010000   jne 0x564966c062f5      ; check 24
│           0x564966c06152      8a442440       mov al, byte [arg_40h]
│           0x564966c06156      880424         mov byte [rsp], al
│           0x564966c06159      8a0424         mov al, byte [rsp]
│           0x564966c0615c      48c704241c00.  mov qword [rsp], 0x1c   ; [0x1c:8]=-1 ; 28
│           0x564966c06164      488b3c24       mov rdi, qword [rsp]
│           0x564966c06168      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c0616c      0f879e030000   ja 0x564966c06510
│           0x564966c06172      488d0d1c3c03.  lea rcx, [0x564966c39d95]
│           0x564966c06179      3a040f         cmp al, byte [rdi + rcx]
│           0x564966c0617c      0f8573010000   jne 0x564966c062f5      ; check 25
│           0x564966c06182      8a442443       mov al, byte [arg_43h]
│           0x564966c06186      880424         mov byte [rsp], al
│           0x564966c06189      8a0424         mov al, byte [rsp]
│           0x564966c0618c      48c704240d00.  mov qword [rsp], 0xd    ; [0xd:8]=-1 ; 13
│           0x564966c06194      488b3c24       mov rdi, qword [rsp]
│           0x564966c06198      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c0619c      0f8785030000   ja 0x564966c06527
│           0x564966c061a2      488d0dec3b03.  lea rcx, [0x564966c39d95]
│           0x564966c061a9      3a040f         cmp al, byte [rdi + rcx]
│           0x564966c061ac      0f8543010000   jne 0x564966c062f5      ; check 26
│           0x564966c061b2      8a442442       mov al, byte [arg_42h]
│           0x564966c061b6      880424         mov byte [rsp], al
│           0x564966c061b9      8a0424         mov al, byte [rsp]
│           0x564966c061bc      48c704241100.  mov qword [rsp], 0x11   ; [0x11:8]=-1 ; 17
│           0x564966c061c4      488b3c24       mov rdi, qword [rsp]
│           0x564966c061c8      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c061cc      0f876c030000   ja 0x564966c0653e
│           0x564966c061d2      488d0dbc3b03.  lea rcx, [0x564966c39d95]
│           0x564966c061d9      3a040f         cmp al, byte [rdi + rcx]
│           0x564966c061dc b    0f8513010000   jne 0x564966c062f5      ; check 27
│           0x564966c061e2      8a442433       mov al, byte [arg_33h]
│           0x564966c061e6      880424         mov byte [rsp], al
│           0x564966c061e9      8a0424         mov al, byte [rsp]
│           0x564966c061ec      48c704240200.  mov qword [rsp], 2
│           0x564966c061f4      488b3c24       mov rdi, qword [rsp]
│           0x564966c061f8      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c061fc      0f8753030000   ja 0x564966c06555
│           0x564966c06202      488d0d8c3b03.  lea rcx, [0x564966c39d95]
│           0x564966c06209      3a040f         cmp al, byte [rdi + rcx]
│           0x564966c0620c      0f85e3000000   jne 0x564966c062f5      ; check 28
│           0x564966c06212      8a442435       mov al, byte [arg_35h]
│           0x564966c06216      880424         mov byte [rsp], al
│           0x564966c06219      8a0424         mov al, byte [rsp]
│           0x564966c0621c      48c704240900.  mov qword [rsp], 9
│           0x564966c06224      488b3c24       mov rdi, qword [rsp]
│           0x564966c06228      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c0622c      0f873a030000   ja 0x564966c0656c
│           0x564966c06232      488d0d5c3b03.  lea rcx, [0x564966c39d95]
│           0x564966c06239      3a040f         cmp al, byte [rdi + rcx]
│           0x564966c0623c      0f85b3000000   jne 0x564966c062f5      ; check 29
│           0x564966c06242      8a442445       mov al, byte [arg_45h]
│           0x564966c06246      880424         mov byte [rsp], al
│           0x564966c06249      8a0424         mov al, byte [rsp]
│           0x564966c0624c      48c704240400.  mov qword [rsp], 4
│           0x564966c06254      488b3c24       mov rdi, qword [rsp]
│           0x564966c06258      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c0625c      0f8721030000   ja 0x564966c06583
│           0x564966c06262      488d0d2c3b03.  lea rcx, [0x564966c39d95]
│           0x564966c06269      3a040f         cmp al, byte [rdi + rcx]
│           0x564966c0626c      0f8583000000   jne 0x564966c062f5      ; check 30
│           0x564966c06272      8a442434       mov al, byte [arg_34h]
│           0x564966c06276      880424         mov byte [rsp], al
│           0x564966c06279      8a0424         mov al, byte [rsp]
│           0x564966c0627c      48c704241800.  mov qword [rsp], 0x18   ; [0x18:8]=-1 ; 24
│           0x564966c06284      488b3c24       mov rdi, qword [rsp]
│           0x564966c06288      4883ff1f       cmp rdi, 0x1f           ; 31
│           0x564966c0628c      0f8708030000   ja 0x564966c0659a
│           0x564966c06292      488d0dfc3a03.  lea rcx, [0x564966c39d95]
│           0x564966c06299      3a040f         cmp al, byte [rdi + rcx]
│           0x564966c0629c      7557           jne 0x564966c062f5      ; check 31
│           0x564966c0629e      8a442444       mov al, byte [arg_44h]
│           0x564966c062a2      880424         mov byte [rsp], al
│           0x564966c062a5      8a0424         mov al, byte [rsp]
│           0x564966c062a8      48c704241200.  mov qword [rsp], 0x12   ; [0x12:8]=-1 ; 18
│           0x564966c062b0      488b3c24       mov rdi, qword [rsp]
│           0x564966c062b4      4883ff20       cmp rdi, 0x20           ; 32
│           0x564966c062b8      0f83f3020000   jae 0x564966c065b1
            0x564966c062be      488d0dd03a03.  lea rcx, [0x564966c39d95]
            0x564966c062c5      3a040f         cmp al, byte [rdi + rcx]
            0x564966c062c8      752b           jne 0x564966c062f5      ; fcn.00005cde+0x617 ; check 32
            0x564966c062ca      e8d1030000     call fcn.000066a0       ; Print 'Success'
            0x564966c062cf      e943f8ffff     jmp 0x564966c05b17      ; fcn.00006436-0x91f
            ; CODE XREF from rip @ +0x19c
            0x564966c062d4      e827030000     call fcn.00006600
            0x564966c062d9      e939f8ffff     jmp 0x564966c05b17      ; fcn.00006436-0x91f
│           ; CODE XREF from fcn.00005cde @ 0x564966c05cf8
│           0x564966c062de      488d152b1f24.  lea rdx, [0x564966e48210]
│           0x564966c062e5      be20000000     mov esi, 0x20           ; 32
│           0x564966c062ea      ff1550482400   call qword [0x564966e4ab40] ; [0x564966e4ab40:8]=0x564966c356a0
│           0x564966c062f0      e922f8ffff     jmp 0x564966c05b17      ; fcn.00006436-0x91f
│           ; XREFS(32)
│           0x564966c062f5      e856030000     call fcn.00006650       ; Print 'Invalid Password'
│           0x564966c062fa      e918f8ffff     jmp 0x564966c05b17      ; fcn.00006436-0x91f
```