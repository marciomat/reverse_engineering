```assembly
            ; DATA XREF from entry0 @ 0x401131
┌ 94: int main (int argc, char **argv, char **envp);
│           ; var int64_t var_10h @ rsp+0x10
│           ; var int64_t var_20h @ rsp+0x20
│           ; var int64_t var_30h @ rsp+0x30
│           ; var int64_t var_40h @ rsp+0x40
│           0x004010b0      55             push rbp
│           0x004010b1      660fefc0       pxor xmm0, xmm0
│           0x004010b5      488d3d700f00.  lea rdi, str.Input:         ; 0x40202c ; "Input:" ; const char *s
│           0x004010bc      4883ec50       sub rsp, 0x50
│           0x004010c0      0f290424       movaps xmmword [rsp], xmm0
│           0x004010c4      4889e5         mov rbp, rsp
│           0x004010c7      0f29442410     movaps xmmword [var_10h], xmm0
│           0x004010cc      0f29442420     movaps xmmword [var_20h], xmm0
│           0x004010d1      0f29442430     movaps xmmword [var_30h], xmm0
│           0x004010d6      c644244000     mov byte [var_40h], 0
│           0x004010db      e850ffffff     call sym.imp.puts           ; int puts(const char *s)
│           0x004010e0      488b15a92f00.  mov rdx, qword [obj.stdin]  ; [0x404090:8]=0 ; FILE *stream
│           0x004010e7      be41000000     mov esi, 0x41               ; 'A' ; 65 ; int size
│           0x004010ec      4889ef         mov rdi, rbp                ; char *s
│           0x004010ef      e86cffffff     call sym.imp.fgets          ; char *fgets(char *s, int size, FILE *stream)
│           0x004010f4      4889ef         mov rdi, rbp                ; const char *s
│           0x004010f7      e854ffffff     call sym.imp.strlen         ; size_t strlen(const char *s)
│           0x004010fc      4889ef         mov rdi, rbp                ; int64_t arg1
│           0x004010ff      89c6           mov esi, eax                ; uint32_t arg2
│           0x00401101      e825040000     call fcn.0040152b
│           0x00401106      4883c450       add rsp, 0x50
│           0x0040110a      31c0           xor eax, eax
│           0x0040110c      5d             pop rbp
└           0x0040110d      c3             ret
```
