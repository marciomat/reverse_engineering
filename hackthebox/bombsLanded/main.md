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
│           0x08048952      81c3de070000   add ebx, 0x7de              ; 2014
│           0x08048958      891d48930408   mov dword [0x8049348], ebx  ; [0x8049348:4]=0; RELOC 32 
│           0x0804895e      c745e04c9304.  mov dword [var_20h], 0x804934c; RELOC 32 
│           0x08048965      c745dc389304.  mov dword [var_24h], 0x8049338; RELOC 32 
│           0x0804896c      c745d83c9304.  mov dword [var_28h], 0x804933c; RELOC 32 
│           0x08048973      c745d4409304.  mov dword [var_2ch], 0x8049340; RELOC 32 
│           0x0804897a      8b45e0         mov eax, dword [var_20h]
│           0x0804897d      8b00           mov eax, dword [eax]
│           0x0804897f      8d4801         lea ecx, [eax + 1]
│           0x08048982      8b45e0         mov eax, dword [var_20h]
│           0x08048985      8908           mov dword [eax], ecx
│           0x08048987      8b45dc         mov eax, dword [var_24h]
│           0x0804898a      8b00           mov eax, dword [eax]
│           0x0804898c      8d48ff         lea ecx, [eax - 1]
│           0x0804898f      8b45dc         mov eax, dword [var_24h]
│           0x08048992      8908           mov dword [eax], ecx
│           0x08048994      8b45d8         mov eax, dword [var_28h]
│           0x08048997      8b00           mov eax, dword [eax]
│           0x08048999      8d4801         lea ecx, [eax + 1]
│           0x0804899c      8b45d8         mov eax, dword [var_28h]
│           0x0804899f      8908           mov dword [eax], ecx
│           0x080489a1      8b45d4         mov eax, dword [var_2ch]
│           0x080489a4      8b00           mov eax, dword [eax]
│           0x080489a6      8d48ff         lea ecx, [eax - 1]
│           0x080489a9      8b45d4         mov eax, dword [var_2ch]
│           0x080489ac      8908           mov dword [eax], ecx
│           0x080489ae      8b45e0         mov eax, dword [var_20h]
│           0x080489b1      8b08           mov ecx, dword [eax]
│           0x080489b3      8b45d8         mov eax, dword [var_28h]
│           0x080489b6      8b00           mov eax, dword [eax]
│           0x080489b8      39c1           cmp ecx, eax
│       ┌─< 0x080489ba      7705           ja 0x80489c1
│       │   0x080489bc      833a04         cmp dword [edx], 4
│      ┌──< 0x080489bf      7f57           jg 0x8048a18
│      ││   ; CODE XREF from main @ 0x80489ba
│      │└─> 0x080489c1      833a03         cmp dword [edx], 3
│      │┌─< 0x080489c4      7e37           jle 0x80489fd
│      ││   0x080489c6      83ec0c         sub esp, 0xc
│      ││   0x080489c9      68708c0408     push 0x8048c70              ; RELOC 32  ; char **argv
│      ││   0x080489ce      e8fcffffff     call printf                 ; RELOC 32 printf ; int main(char **argv)
│      ││   0x080489d3      83c410         add esp, 0x10
│      ││   0x080489d6      e8fcffffff     call getchar                ; RELOC 32 getchar ; int main(char **argv)
│      ││   0x080489db      8845cf         mov byte [var_31h], al
│      ││   0x080489de      807dcf58       cmp byte [var_31h], 0x58
│     ┌───< 0x080489e2      751a           jne 0x80489fe
│     │││   0x080489e4      a1148a0408     mov eax, dword [0x8048a14]  ; [0x8048a14:4]=195
│     │││   0x080489e9      ffd0           call eax
│     │││   0x080489eb      83ec0c         sub esp, 0xc
│     │││   0x080489ee      68818c0408     push 0x8048c81              ; RELOC 32  ; char **argv
│     │││   0x080489f3      e8fcffffff     call __isoc99_scanf         ; RELOC 32 __isoc99_scanf ; int main(char **argv)
│     │││   0x080489f8      83c410         add esp, 0x10
│    ┌────< 0x080489fb      eb01           jmp 0x80489fe
│    ││││   ; CODE XREF from main @ 0x80489c4
│    │││└─> 0x080489fd      90             nop
│    │││    ; CODE XREFS from main @ 0x80489e2, 0x80489fb
│    └└───> 0x080489fe      83ec0c         sub esp, 0xc
│      │    0x08048a01      68938c0408     push 0x8048c93              ; RELOC 32  ; char **argv
│      │    0x08048a06      e8fcffffff     call puts                   ; RELOC 32 puts ; int main(char **argv)
│      │    0x08048a0b      83c410         add esp, 0x10
│      │    0x08048a0e      b800000000     mov eax, 0
│      │┌─< 0x08048a13      e9c3000000     jmp 0x8048adb
│      ││   ; CODE XREF from main @ 0x80489bf
│      └──> 0x08048a18      90             nop
│       │   0x08048a19      83ec08         sub esp, 8
│       │   0x08048a1c      6a00           push 0
│       │   0x08048a1e      6aff           push 0xffffffffffffffff
│       │   0x08048a20      6a22           push 0x22                   ; '\"' ; 34
│       │   0x08048a22      6a07           push 7                      ; 7
│       │   0x08048a24      6800100000     push 0x1000
│       │   0x08048a29      6a00           push 0                      ; char **argv
│       │   0x08048a2b      e8fcffffff     call mmap                   ; RELOC 32 mmap ; int main(char **argv)
│       │   0x08048a30      83c420         add esp, 0x20
│       │   0x08048a33      8945d0         mov dword [var_30h], eax
│       │   0x08048a36      83ec04         sub esp, 4
│       │   0x08048a39      6800100000     push 0x1000
│       │   0x08048a3e      68c3000000     push 0xc3                   ; 195
│       │   0x08048a43      ff75d0         push dword [var_30h]        ; char **argv
│       │   0x08048a46      e8fcffffff     call memset                 ; RELOC 32 memset ; int main(char **argv)
│       │   0x08048a4b      83c410         add esp, 0x10
│       │   0x08048a4e      8b45d0         mov eax, dword [var_30h]
│       │   0x08048a51      bba0910408     mov ebx, 0x80491a0          ; RELOC 32 
│       │   0x08048a56      ba97010000     mov edx, 0x197              ; 407
│       │   0x08048a5b      8b0b           mov ecx, dword [ebx]
│       │   0x08048a5d      8908           mov dword [eax], ecx
│       │   0x08048a5f      8b4c13fc       mov ecx, dword [ebx + edx - 4]
│       │   0x08048a63      894c10fc       mov dword [eax + edx - 4], ecx
│       │   0x08048a67      8d7804         lea edi, [eax + 4]
│       │   0x08048a6a      83e7fc         and edi, 0xfffffffc         ; 4294967292
│       │   0x08048a6d      29f8           sub eax, edi
│       │   0x08048a6f      29c3           sub ebx, eax
│       │   0x08048a71      01c2           add edx, eax
│       │   0x08048a73      83e2fc         and edx, 0xfffffffc         ; 4294967292
│       │   0x08048a76      89d0           mov eax, edx
│       │   0x08048a78      c1e802         shr eax, 2
│       │   0x08048a7b      89de           mov esi, ebx
│       │   0x08048a7d      89c1           mov ecx, eax
│       │   0x08048a7f      f3a5           rep movsd dword es:[edi], dword ptr [esi]
│       │   0x08048a81      c745e4000000.  mov dword [var_1ch], 0
│      ┌──< 0x08048a88      eb1c           jmp 0x8048aa6
│      ││   ; CODE XREF from main @ 0x8048aae
│     ┌───> 0x08048a8a      8b55e4         mov edx, dword [var_1ch]
│     ╎││   0x08048a8d      8b45d0         mov eax, dword [var_30h]
│     ╎││   0x08048a90      01d0           add eax, edx
│     ╎││   0x08048a92      8b4de4         mov ecx, dword [var_1ch]
│     ╎││   0x08048a95      8b55d0         mov edx, dword [var_30h]
│     ╎││   0x08048a98      01ca           add edx, ecx
│     ╎││   0x08048a9a      0fb612         movzx edx, byte [edx]
│     ╎││   0x08048a9d      83f263         xor edx, 0x63               ; 99
│     ╎││   0x08048aa0      8810           mov byte [eax], dl
│     ╎││   0x08048aa2      8345e401       add dword [var_1ch], 1
│     ╎││   ; CODE XREF from main @ 0x8048a88
│     ╎└──> 0x08048aa6      8b45e4         mov eax, dword [var_1ch]
│     ╎ │   0x08048aa9      3d96010000     cmp eax, 0x196              ; 406
│     └───< 0x08048aae      76da           jbe 0x8048a8a
│       │   0x08048ab0      a148930408     mov eax, dword [0x8049348]  ; [0x8049348:4]=0; RELOC 32 
│       │   0x08048ab5      89c3           mov ebx, eax
│       │   0x08048ab7      8b45d0         mov eax, dword [var_30h]
│       │   0x08048aba      ffd0           call eax
│       │   0x08048abc      83ec04         sub esp, 4
│       │   0x08048abf      6897010000     push 0x197                  ; 407
│       │   0x08048ac4      6a00           push 0
│       │   0x08048ac6      ff75d0         push dword [var_30h]        ; char **argv
│       │   0x08048ac9      e8fcffffff     call memset                 ; RELOC 32 memset ; int main(char **argv)
│       │   0x08048ace      83c410         add esp, 0x10
│       │   0x08048ad1      83ec0c         sub esp, 0xc
│       │   0x08048ad4      6a00           push 0                      ; char **argv
│       │   0x08048ad6      e8fcffffff     call exit                   ; RELOC 32 exit ; int main(char **argv)
│       │   ; CODE XREF from main @ 0x8048a13
│       └─> 0x08048adb      8d65f0         lea esp, [var_10h]
│           0x08048ade      59             pop ecx
│           0x08048adf      5b             pop ebx
│           0x08048ae0      5e             pop esi
│           0x08048ae1      5f             pop edi
│           0x08048ae2      5d             pop ebp
│           0x08048ae3      8d61fc         lea esp, [ecx - 4]
└           0x08048ae6      c3             ret
```
