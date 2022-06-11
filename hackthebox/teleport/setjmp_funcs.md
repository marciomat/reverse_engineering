```assembly
            0x00000b2a      55             push rbp
            0x00000b2b      4889e5         mov rbp, rsp
            0x00000b2e      488d3d232a20.  lea rdi, [0x00203558]
            0x00000b35      e8b6feffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00000b3a      85c0           test eax, eax
        ┌─< 0x00000b3c      742d           je 0xb6b
        │   0x00000b3e      0fb6053e2720.  movzx eax, byte [0x00203283] ; [0x203283:1]=0
        │   0x00000b45      3c7b           cmp al, 0x7b
       ┌──< 0x00000b47      7511           jne 0xb5a
       ││   0x00000b49      be04000000     mov esi, 4
       ││   0x00000b4e      488d3d4b2620.  lea rdi, [0x002031a0]
       ││   0x00000b55      e8a6feffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
       ││   ; CODE XREF from entry.init0 @ +0x27
       └──> 0x00000b5a      be65000000     mov esi, 0x65               ; 'e'
        │   0x00000b5f      488d3d3a2620.  lea rdi, [0x002031a0]
        │   0x00000b66      e895feffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
        │   ; CODE XREF from entry.init0 @ +0x1c
        └─> 0x00000b6b      90             nop
            0x00000b6c      5d             pop rbp
            0x00000b6d      c3             ret
            0x00000b6e      55             push rbp
            0x00000b6f      4889e5         mov rbp, rsp
            0x00000b72      488d3d6f2b20.  lea rdi, [0x002036e8]
            0x00000b79      e872feffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00000b7e      85c0           test eax, eax
        ┌─< 0x00000b80      742d           je 0xbaf
        │   0x00000b82      0fb605fc2620.  movzx eax, byte [0x00203285] ; [0x203285:1]=0
        │   0x00000b89      3c75           cmp al, 0x75
       ┌──< 0x00000b8b      7511           jne 0xb9e
       ││   0x00000b8d      be06000000     mov esi, 6
       ││   0x00000b92      488d3d072620.  lea rdi, [0x002031a0]
       ││   0x00000b99      e862feffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
       ││   ; CODE XREF from entry.init0 @ +0x6b
       └──> 0x00000b9e      be65000000     mov esi, 0x65               ; 'e'
        │   0x00000ba3      488d3df62520.  lea rdi, [0x002031a0]
        │   0x00000baa      e851feffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
        │   ; CODE XREF from entry.init0 @ +0x60
        └─> 0x00000baf      90             nop
            0x00000bb0      5d             pop rbp
            0x00000bb1      c3             ret
            0x00000bb2      55             push rbp
            0x00000bb3      4889e5         mov rbp, rsp
            0x00000bb6      488d3d5b3c20.  lea rdi, [0x00204818]
            0x00000bbd      e82efeffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00000bc2      85c0           test eax, eax
        ┌─< 0x00000bc4      742d           je 0xbf3
        │   0x00000bc6      0fb605ce2620.  movzx eax, byte [0x0020329b] ; [0x20329b:1]=0
        │   0x00000bcd      3c74           cmp al, 0x74
       ┌──< 0x00000bcf      7511           jne 0xbe2
       ││   0x00000bd1      be1c000000     mov esi, 0x1c
       ││   0x00000bd6      488d3dc32520.  lea rdi, [0x002031a0]
       ││   0x00000bdd      e81efeffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
       ││   ; CODE XREF from entry.init0 @ +0xaf
       └──> 0x00000be2      be65000000     mov esi, 0x65               ; 'e'
        │   0x00000be7      488d3db22520.  lea rdi, [0x002031a0]
        │   0x00000bee      e80dfeffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
        │   ; CODE XREF from entry.init0 @ +0xa4
        └─> 0x00000bf3      90             nop
            0x00000bf4      5d             pop rbp
            0x00000bf5      c3             ret
            0x00000bf6      55             push rbp
            0x00000bf7      4889e5         mov rbp, rsp
            0x00000bfa      488d3d574220.  lea rdi, [0x00204e58]
            0x00000c01      e8eafdffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00000c06      85c0           test eax, eax
        ┌─< 0x00000c08      742d           je 0xc37
        │   0x00000c0a      0fb605922620.  movzx eax, byte [0x002032a3] ; [0x2032a3:1]=0
        │   0x00000c11      3c74           cmp al, 0x74
       ┌──< 0x00000c13      7511           jne 0xc26
       ││   0x00000c15      be24000000     mov esi, 0x24               ; '$'
       ││   0x00000c1a      488d3d7f2520.  lea rdi, [0x002031a0]
       ││   0x00000c21      e8dafdffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
       ││   ; CODE XREF from entry.init0 @ +0xf3
       └──> 0x00000c26      be65000000     mov esi, 0x65               ; 'e'
        │   0x00000c2b      488d3d6e2520.  lea rdi, [0x002031a0]
        │   0x00000c32      e8c9fdffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
        │   ; CODE XREF from entry.init0 @ +0xe8
        └─> 0x00000c37      90             nop
            0x00000c38      5d             pop rbp
            0x00000c39      c3             ret
            0x00000c3a      55             push rbp
            0x00000c3b      4889e5         mov rbp, rsp
            0x00000c3e      488d3de33020.  lea rdi, [0x00203d28]
            0x00000c45      e8a6fdffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00000c4a      85c0           test eax, eax
        ┌─< 0x00000c4c      742d           je 0xc7b
        │   0x00000c4e      0fb605382620.  movzx eax, byte [0x0020328d] ; [0x20328d:1]=0
        │   0x00000c55      3c68           cmp al, 0x68
        │   0x00000c57      7511           jne 0xc6a
        │   0x00000c59      be0e000000     mov esi, 0xe
        │   0x00000c5e      488d3d3b2520.  lea rdi, [0x002031a0]
        │   0x00000c65      e896fdffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
        │   ; CODE XREF from entry.init0 @ +0x137
        │   0x00000c6a      be65000000     mov esi, 0x65               ; 'e'
        │   0x00000c6f      488d3d2a2520.  lea rdi, [0x002031a0]
        │   0x00000c76      e885fdffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
        │   ; CODE XREF from entry.init0 @ +0x12c
        └─> 0x00000c7b      90             nop
            0x00000c7c      5d             pop rbp
            0x00000c7d      c3             ret
            0x00000c7e      55             push rbp
            0x00000c7f      4889e5         mov rbp, rsp
            0x00000c82      488d3d0f2f20.  lea rdi, [0x00203b98]
            0x00000c89      e862fdffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00000c8e      85c0           test eax, eax
            0x00000c90      742d           je 0xcbf
            0x00000c92      0fb605f22520.  movzx eax, byte [0x0020328b] ; [0x20328b:1]=0
            0x00000c99      3c5f           cmp al, 0x5f
            0x00000c9b      7511           jne 0xcae
            0x00000c9d      be0c000000     mov esi, 0xc
            0x00000ca2      488d3df72420.  lea rdi, [0x002031a0]
            0x00000ca9      e852fdffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x17b
            0x00000cae      be65000000     mov esi, 0x65               ; 'e'
            0x00000cb3      488d3de62420.  lea rdi, [0x002031a0]
            0x00000cba      e841fdffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x170
            0x00000cbf      90             nop
            0x00000cc0      5d             pop rbp
            0x00000cc1      c3             ret
            0x00000cc2      55             push rbp
            0x00000cc3      4889e5         mov rbp, rsp
            0x00000cc6      488d3d233120.  lea rdi, [0x00203df0]
            0x00000ccd      e81efdffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00000cd2      85c0           test eax, eax
            0x00000cd4      742d           je 0xd03
            0x00000cd6      0fb605b12520.  movzx eax, byte [0x0020328e] ; [0x20328e:1]=0
            0x00000cdd      3c72           cmp al, 0x72
            0x00000cdf      7511           jne 0xcf2
            0x00000ce1      be0f000000     mov esi, 0xf
            0x00000ce6      488d3db32420.  lea rdi, [0x002031a0]
            0x00000ced      e80efdffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x1bf
            0x00000cf2      be65000000     mov esi, 0x65               ; 'e'
            0x00000cf7      488d3da22420.  lea rdi, [0x002031a0]
            0x00000cfe      e8fdfcffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x1b4
            0x00000d03      90             nop
            0x00000d04      5d             pop rbp
            0x00000d05      c3             ret
            0x00000d06      55             push rbp
            0x00000d07      4889e5         mov rbp, rsp
            0x00000d0a      488d3d7f2720.  lea rdi, [0x00203490]
            0x00000d11      e8dafcffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00000d16      85c0           test eax, eax
            0x00000d18      742d           je 0xd47
            0x00000d1a      0fb605612520.  movzx eax, byte [0x00203282] ; [0x203282:1]=0
            0x00000d21      3c42           cmp al, 0x42
            0x00000d23      7511           jne 0xd36
            0x00000d25      be03000000     mov esi, 3
            0x00000d2a      488d3d6f2420.  lea rdi, [0x002031a0]
            0x00000d31      e8cafcffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x203
            0x00000d36      be65000000     mov esi, 0x65               ; 'e'
            0x00000d3b      488d3d5e2420.  lea rdi, [0x002031a0]
            0x00000d42      e8b9fcffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x1f8
            0x00000d47      90             nop
            0x00000d48      5d             pop rbp
            0x00000d49      c3             ret
            0x00000d4a      55             push rbp
            0x00000d4b      4889e5         mov rbp, rsp
            0x00000d4e      488d3dcb2820.  lea rdi, [0x00203620]
            0x00000d55      e896fcffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00000d5a      85c0           test eax, eax
            0x00000d5c      742d           je 0xd8b
            0x00000d5e      0fb6051f2520.  movzx eax, byte [0x00203284] ; [0x203284:1]=0
            0x00000d65      3c6a           cmp al, 0x6a
            0x00000d67      7511           jne 0xd7a
            0x00000d69      be05000000     mov esi, 5
            0x00000d6e      488d3d2b2420.  lea rdi, [0x002031a0]
            0x00000d75      e886fcffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x247
            0x00000d7a      be65000000     mov esi, 0x65               ; 'e'
            0x00000d7f      488d3d1a2420.  lea rdi, [0x002031a0]
            0x00000d86      e875fcffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x23c
            0x00000d8b      90             nop
            0x00000d8c      5d             pop rbp
            0x00000d8d      c3             ret
            0x00000d8e      55             push rbp
            0x00000d8f      4889e5         mov rbp, rsp
            0x00000d92      488d3d4f4220.  lea rdi, [0x00204fe8]
            0x00000d99      e852fcffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00000d9e      85c0           test eax, eax
            0x00000da0      742d           je 0xdcf
            0x00000da2      0fb605fc2420.  movzx eax, byte [0x002032a5] ; [0x2032a5:1]=0
            0x00000da9      3c6e           cmp al, 0x6e
            0x00000dab      7511           jne 0xdbe
            0x00000dad      be26000000     mov esi, 0x26               ; '&'
            0x00000db2      488d3de72320.  lea rdi, [0x002031a0]
            0x00000db9      e842fcffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x28b
            0x00000dbe      be65000000     mov esi, 0x65               ; 'e'
            0x00000dc3      488d3dd62320.  lea rdi, [0x002031a0]
            ; DATA XREF from entry0 @ 0xa2f
            0x00000dca      e831fcffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x280
            0x00000dcf      90             nop
            0x00000dd0      5d             pop rbp
            0x00000dd1      c3             ret
            0x00000dd2      55             push rbp
            0x00000dd3      4889e5         mov rbp, rsp
            0x00000dd6      488d3d832e20.  lea rdi, [0x00203c60]
            0x00000ddd      e80efcffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00000de2      85c0           test eax, eax
            0x00000de4      742d           je 0xe13
            0x00000de6      0fb6059f2420.  movzx eax, byte [0x0020328c] ; [0x20328c:1]=0
            0x00000ded      3c74           cmp al, 0x74
            0x00000def      7511           jne 0xe02
            0x00000df1      be0d000000     mov esi, 0xd
            0x00000df6      488d3da32320.  lea rdi, [0x002031a0]
            0x00000dfd      e8fefbffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x2cf
            0x00000e02      be65000000     mov esi, 0x65               ; 'e'
            0x00000e07      488d3d922320.  lea rdi, [0x002031a0]
            0x00000e0e      e8edfbffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x2c4
            0x00000e13      90             nop
            0x00000e14      5d             pop rbp
            0x00000e15      c3             ret
            0x00000e16      55             push rbp
            0x00000e17      4889e5         mov rbp, rsp
            0x00000e1a      488d3d0f3620.  lea rdi, [0x00204430]
            0x00000e21      e8cafbffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00000e26      85c0           test eax, eax
            0x00000e28      742d           je 0xe57
            0x00000e2a      0fb605652420.  movzx eax, byte [0x00203296] ; [0x203296:1]=0
            0x00000e31      3c70           cmp al, 0x70
            0x00000e33      7511           jne 0xe46
            0x00000e35      be17000000     mov esi, 0x17
            0x00000e3a      488d3d5f2320.  lea rdi, [0x002031a0]
            0x00000e41      e8bafbffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x313
            0x00000e46      be65000000     mov esi, 0x65               ; 'e'
            0x00000e4b      488d3d4e2320.  lea rdi, [0x002031a0]
            0x00000e52      e8a9fbffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x308
            0x00000e57      90             nop
            0x00000e58      5d             pop rbp
            0x00000e59      c3             ret
            0x00000e5a      55             push rbp
            0x00000e5b      4889e5         mov rbp, rsp
            0x00000e5e      488d3d5b3720.  lea rdi, [0x002045c0]
            0x00000e65      e886fbffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00000e6a      85c0           test eax, eax
            0x00000e6c      742d           je 0xe9b
            0x00000e6e      0fb605232420.  movzx eax, byte [0x00203298] ; [0x203298:1]=0
            0x00000e75      3c63           cmp al, 0x63
            0x00000e77      7511           jne 0xe8a
            0x00000e79      be19000000     mov esi, 0x19
            0x00000e7e      488d3d1b2320.  lea rdi, [0x002031a0]
            0x00000e85      e876fbffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x357
            0x00000e8a      be65000000     mov esi, 0x65               ; 'e'
            0x00000e8f      488d3d0a2320.  lea rdi, [0x002031a0]
            0x00000e96      e865fbffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x34c
            0x00000e9b      90             nop
            0x00000e9c      5d             pop rbp
            0x00000e9d      c3             ret
            0x00000e9e      55             push rbp
            0x00000e9f      4889e5         mov rbp, rsp
            0x00000ea2      488d3df73320.  lea rdi, [0x002042a0]
            0x00000ea9      e842fbffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00000eae      85c0           test eax, eax
            0x00000eb0      742d           je 0xedf
            0x00000eb2      0fb605db2320.  movzx eax, byte [0x00203294] ; [0x203294:1]=0
            0x00000eb9      3c5f           cmp al, 0x5f
            0x00000ebb      7511           jne 0xece
            0x00000ebd      be15000000     mov esi, 0x15
            0x00000ec2      488d3dd72220.  lea rdi, [0x002031a0]
            0x00000ec9      e832fbffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x39b
            0x00000ece      be65000000     mov esi, 0x65               ; 'e'
            0x00000ed3      488d3dc62220.  lea rdi, [0x002031a0]
            0x00000eda      e821fbffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x390
            0x00000edf      90             nop
            0x00000ee0      5d             pop rbp
            0x00000ee1      c3             ret
            0x00000ee2      55             push rbp
            0x00000ee3      4889e5         mov rbp, rsp
            0x00000ee6      488d3d1b2b20.  lea rdi, [0x00203a08]
            0x00000eed      e8fefaffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00000ef2      85c0           test eax, eax
            0x00000ef4      742d           je 0xf23
            0x00000ef6      0fb6058c2320.  movzx eax, byte [0x00203289] ; [0x203289:1]=0
            0x00000efd      3c6e           cmp al, 0x6e
            0x00000eff      7511           jne 0xf12
            0x00000f01      be0a000000     mov esi, 0xa
            0x00000f06      488d3d932220.  lea rdi, [0x002031a0]
            0x00000f0d      e8eefaffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x3df
            0x00000f12      be65000000     mov esi, 0x65               ; 'e'
            0x00000f17      488d3d822220.  lea rdi, [0x002031a0]
            0x00000f1e      e8ddfaffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x3d4
            0x00000f23      90             nop
            0x00000f24      5d             pop rbp
            0x00000f25      c3             ret
            0x00000f26      55             push rbp
            0x00000f27      4889e5         mov rbp, rsp
            0x00000f2a      488d3d0f4320.  lea rdi, [0x00205240]
            0x00000f31      e8bafaffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00000f36      85c0           test eax, eax
            0x00000f38      742d           je 0xf67
            0x00000f3a      0fb605672320.  movzx eax, byte [0x002032a8] ; [0x2032a8:1]=0
            0x00000f41      3c6d           cmp al, 0x6d
            0x00000f43      7511           jne 0xf56
            0x00000f45      be29000000     mov esi, 0x29               ; ')'
            0x00000f4a      488d3d4f2220.  lea rdi, [0x002031a0]
            0x00000f51      e8aafaffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x423
            0x00000f56      be65000000     mov esi, 0x65               ; 'e'
            0x00000f5b      488d3d3e2220.  lea rdi, [0x002031a0]
            0x00000f62      e899faffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x418
            0x00000f67      90             nop
            0x00000f68      5d             pop rbp
            0x00000f69      c3             ret
            0x00000f6a      55             push rbp
            0x00000f6b      4889e5         mov rbp, rsp
            0x00000f6e      488d3d3b4120.  lea rdi, [0x002050b0]
            0x00000f75      e876faffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00000f7a      85c0           test eax, eax
            0x00000f7c      742d           je 0xfab
            0x00000f7e      0fb605212320.  movzx eax, byte [0x002032a6] ; [0x2032a6:1]=0
            0x00000f85      3c75           cmp al, 0x75
            0x00000f87      7511           jne 0xf9a
            0x00000f89      be27000000     mov esi, 0x27               ; '''
            0x00000f8e      488d3d0b2220.  lea rdi, [0x002031a0]
            0x00000f95      e866faffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x467
            0x00000f9a      be65000000     mov esi, 0x65               ; 'e'
            0x00000f9f      488d3dfa2120.  lea rdi, [0x002031a0]
            0x00000fa6      e855faffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x45c
            0x00000fab      90             nop
            0x00000fac      5d             pop rbp
            0x00000fad      c3             ret
            0x00000fae      55             push rbp
            0x00000faf      4889e5         mov rbp, rsp
            0x00000fb2      488d3dd73d20.  lea rdi, [0x00204d90]
            0x00000fb9      e832faffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00000fbe      85c0           test eax, eax
            0x00000fc0      742d           je 0xfef
            0x00000fc2      0fb605d92220.  movzx eax, byte [0x002032a2] ; [0x2032a2:1]=0
            0x00000fc9      3c6e           cmp al, 0x6e
            0x00000fcb      7511           jne 0xfde
            0x00000fcd      be23000000     mov esi, 0x23               ; '#'
            0x00000fd2      488d3dc72120.  lea rdi, [0x002031a0]
            0x00000fd9      e822faffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x4ab
            0x00000fde      be65000000     mov esi, 0x65               ; 'e'
            0x00000fe3      488d3db62120.  lea rdi, [0x002031a0]
            0x00000fea      e811faffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x4a0
            0x00000fef      90             nop
            0x00000ff0      5d             pop rbp
            0x00000ff1      c3             ret
            0x00000ff2      55             push rbp
            0x00000ff3      4889e5         mov rbp, rsp
            0x00000ff6      488d3d0b4320.  lea rdi, [0x00205308]
            0x00000ffd      e8eef9ffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00001002      85c0           test eax, eax
            0x00001004      742d           je 0x1033
            0x00001006      0fb6059c2220.  movzx eax, byte [0x002032a9] ; [0x2032a9:1]=0
            0x0000100d      3c21           cmp al, 0x21
            0x0000100f      7511           jne 0x1022
            0x00001011      be2a000000     mov esi, 0x2a               ; '*'
            0x00001016      488d3d832120.  lea rdi, [0x002031a0]
            0x0000101d      e8def9ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x4ef
            0x00001022      be65000000     mov esi, 0x65               ; 'e'
            0x00001027      488d3d722120.  lea rdi, [0x002031a0]
            0x0000102e      e8cdf9ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x4e4
            0x00001033      90             nop
            0x00001034      5d             pop rbp
            0x00001035      c3             ret
            0x00001036      55             push rbp
            0x00001037      4889e5         mov rbp, rsp
            0x0000103a      488d3dcf3020.  lea rdi, [0x00204110]
            0x00001041      e8aaf9ffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00001046      85c0           test eax, eax
            0x00001048      742d           je 0x1077
            0x0000104a      0fb605412220.  movzx eax, byte [0x00203292] ; [0x203292:1]=0
            0x00001051      3c68           cmp al, 0x68
            0x00001053      7511           jne 0x1066
            0x00001055      be13000000     mov esi, 0x13
            0x0000105a      488d3d3f2120.  lea rdi, [0x002031a0]
            0x00001061      e89af9ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x533
            0x00001066      be65000000     mov esi, 0x65               ; 'e'
            0x0000106b      488d3d2e2120.  lea rdi, [0x002031a0]
            0x00001072      e889f9ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x528
            0x00001077      90             nop
            0x00001078      5d             pop rbp
            0x00001079      c3             ret
            0x0000107a      55             push rbp
            0x0000107b      4889e5         mov rbp, rsp
            0x0000107e      488d3d433c20.  lea rdi, [0x00204cc8]
            0x00001085      e866f9ffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x0000108a      85c0           test eax, eax
            0x0000108c      742d           je 0x10bb
            0x0000108e      0fb6050c2220.  movzx eax, byte [0x002032a1] ; [0x2032a1:1]=0
            0x00001095      3c30           cmp al, 0x30
            0x00001097      7511           jne 0x10aa
            0x00001099      be22000000     mov esi, 0x22               ; '\"'
            0x0000109e      488d3dfb2020.  lea rdi, [0x002031a0]
            0x000010a5      e856f9ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x577
            0x000010aa      be65000000     mov esi, 0x65               ; 'e'
            0x000010af      488d3dea2020.  lea rdi, [0x002031a0]
            0x000010b6      e845f9ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x56c
            0x000010bb      90             nop
            0x000010bc      5d             pop rbp
            0x000010bd      c3             ret
            0x000010be      55             push rbp
            0x000010bf      4889e5         mov rbp, rsp
            0x000010c2      488d3d173820.  lea rdi, [0x002048e0]
            0x000010c9      e822f9ffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x000010ce      85c0           test eax, eax
            0x000010d0      742d           je 0x10ff
            0x000010d2      0fb605c32120.  movzx eax, byte [0x0020329c] ; [0x20329c:1]=0
            0x000010d9      3c31           cmp al, 0x31
            0x000010db      7511           jne 0x10ee
            0x000010dd      be1d000000     mov esi, 0x1d
            0x000010e2      488d3db72020.  lea rdi, [0x002031a0]
            0x000010e9      e812f9ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x5bb
            0x000010ee      be65000000     mov esi, 0x65               ; 'e'
            0x000010f3      488d3da62020.  lea rdi, [0x002031a0]
            0x000010fa      e801f9ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x5b0
            0x000010ff      90             nop
            0x00001100      5d             pop rbp
            0x00001101      c3             ret
            0x00001102      55             push rbp
            0x00001103      4889e5         mov rbp, rsp
            0x00001106      488d3d433620.  lea rdi, [0x00204750]
            0x0000110d      e8def8ffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00001112      85c0           test eax, eax
            0x00001114      742d           je 0x1143
            0x00001116      0fb6057d2120.  movzx eax, byte [0x0020329a] ; [0x20329a:1]=0
            0x0000111d      3c5f           cmp al, 0x5f
            0x0000111f      7511           jne 0x1132
            0x00001121      be1b000000     mov esi, 0x1b
            0x00001126      488d3d732020.  lea rdi, [0x002031a0]
            0x0000112d      e8cef8ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x5ff
            0x00001132      be65000000     mov esi, 0x65               ; 'e'
            0x00001137      488d3d622020.  lea rdi, [0x002031a0]
            0x0000113e      e8bdf8ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x5f4
            0x00001143      90             nop
            0x00001144      5d             pop rbp
            0x00001145      c3             ret
            0x00001146      55             push rbp
            0x00001147      4889e5         mov rbp, rsp
            0x0000114a      488d3daf3a20.  lea rdi, [0x00204c00]
            0x00001151      e89af8ffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00001156      85c0           test eax, eax
            0x00001158      742d           je 0x1187
            0x0000115a      0fb6053f2120.  movzx eax, byte [0x002032a0] ; [0x2032a0:1]=0
            0x00001161      3c63           cmp al, 0x63
            0x00001163      7511           jne 0x1176
            0x00001165      be21000000     mov esi, 0x21               ; '!'
            0x0000116a      488d3d2f2020.  lea rdi, [0x002031a0]
            0x00001171      e88af8ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x643
            0x00001176      be65000000     mov esi, 0x65               ; 'e'
            0x0000117b      488d3d1e2020.  lea rdi, [0x002031a0]
            0x00001182      e879f8ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x638
            0x00001187      90             nop
            0x00001188      5d             pop rbp
            0x00001189      c3             ret
            0x0000118a      55             push rbp
            0x0000118b      4889e5         mov rbp, rsp
            0x0000118e      488d3d3b2920.  lea rdi, [0x00203ad0]
            0x00001195      e856f8ffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x0000119a      85c0           test eax, eax
            0x0000119c      742d           je 0x11cb
            0x0000119e      0fb605e52020.  movzx eax, byte [0x0020328a] ; [0x20328a:1]=0
            0x000011a5      3c67           cmp al, 0x67
            0x000011a7      7511           jne 0x11ba
            0x000011a9      be0b000000     mov esi, 0xb
            0x000011ae      488d3deb1f20.  lea rdi, [0x002031a0]
            0x000011b5      e846f8ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x687
            0x000011ba      be65000000     mov esi, 0x65               ; 'e'
            0x000011bf      488d3dda1f20.  lea rdi, [0x002031a0]
            0x000011c6      e835f8ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x67c
            0x000011cb      90             nop
            0x000011cc      5d             pop rbp
            0x000011cd      c3             ret
            0x000011ce      55             push rbp
            0x000011cf      4889e5         mov rbp, rsp
            0x000011d2      488d3d272120.  lea rdi, [0x00203300]
            0x000011d9      e812f8ffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x000011de      85c0           test eax, eax
            0x000011e0      742d           je 0x120f
            0x000011e2      0fb605972020.  movzx eax, byte [203280] ; [203280:1]=0
            0x000011e9      3c48           cmp al, 0x48
            0x000011eb      7511           jne 0x11fe
            0x000011ed      be01000000     mov esi, 1
            0x000011f2      488d3da71f20.  lea rdi, [0x002031a0]
            0x000011f9      e802f8ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x6cb
            0x000011fe      be65000000     mov esi, 0x65               ; 'e'
            0x00001203      488d3d961f20.  lea rdi, [0x002031a0]
            0x0000120a      e8f1f7ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x6c0
            0x0000120f      90             nop
            0x00001210      5d             pop rbp
            0x00001211      c3             ret
            0x00001212      55             push rbp
            0x00001213      4889e5         mov rbp, rsp
            0x00001216      488d3d8b3720.  lea rdi, [0x002049a8]
            0x0000121d      e8cef7ffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00001222      85c0           test eax, eax
            0x00001224      742d           je 0x1253
            0x00001226      0fb605702020.  movzx eax, byte [0x0020329d] ; [0x20329d:1]=0
            0x0000122d      3c6d           cmp al, 0x6d
            0x0000122f      7511           jne 0x1242
            0x00001231      be1e000000     mov esi, 0x1e
            0x00001236      488d3d631f20.  lea rdi, [0x002031a0]
            0x0000123d      e8bef7ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x70f
            0x00001242      be65000000     mov esi, 0x65               ; 'e'
            0x00001247      488d3d521f20.  lea rdi, [0x002031a0]
            0x0000124e      e8adf7ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x704
            0x00001253      90             nop
            0x00001254      5d             pop rbp
            0x00001255      c3             ret
            0x00001256      55             push rbp
            0x00001257      4889e5         mov rbp, rsp
            0x0000125a      488d3d672120.  lea rdi, [0x002033c8]
            0x00001261      e88af7ffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00001266      85c0           test eax, eax
            0x00001268      742d           je 0x1297
            0x0000126a      0fb605102020.  movzx eax, byte [0x00203281] ; [0x203281:1]=0
            0x00001271      3c54           cmp al, 0x54
            0x00001273      7511           jne 0x1286
            0x00001275      be02000000     mov esi, 2
            0x0000127a      488d3d1f1f20.  lea rdi, [0x002031a0]
            0x00001281      e87af7ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x753
            0x00001286      be65000000     mov esi, 0x65               ; 'e'
            0x0000128b      488d3d0e1f20.  lea rdi, [0x002031a0]
            0x00001292      e869f7ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x748
            0x00001297      90             nop
            0x00001298      5d             pop rbp
            0x00001299      c3             ret
            0x0000129a      55             push rbp
            0x0000129b      4889e5         mov rbp, rsp
            0x0000129e      488d3de33320.  lea rdi, [0x00204688]
            0x000012a5      e846f7ffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x000012aa      85c0           test eax, eax
            0x000012ac      742d           je 0x12db
            0x000012ae      0fb605e41f20.  movzx eax, byte [0x00203299] ; [0x203299:1]=0
            0x000012b5      3c33           cmp al, 0x33
            0x000012b7      7511           jne 0x12ca
            0x000012b9      be1a000000     mov esi, 0x1a
            0x000012be      488d3ddb1e20.  lea rdi, [0x002031a0]
            0x000012c5      e836f7ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x797
            0x000012ca      be65000000     mov esi, 0x65               ; 'e'
            0x000012cf      488d3dca1e20.  lea rdi, [0x002031a0]
            0x000012d6      e825f7ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x78c
            0x000012db      90             nop
            0x000012dc      5d             pop rbp
            0x000012dd      c3             ret
            0x000012de      55             push rbp
            0x000012df      4889e5         mov rbp, rsp
            0x000012e2      488d3d0f3220.  lea rdi, [0x002044f8]
            0x000012e9      e802f7ffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x000012ee      85c0           test eax, eax
            0x000012f0      742d           je 0x131f
            0x000012f2      0fb6059e1f20.  movzx eax, byte [0x00203297] ; [0x203297:1]=0
            0x000012f9      3c34           cmp al, 0x34
            0x000012fb      7511           jne 0x130e
            0x000012fd      be18000000     mov esi, 0x18
            0x00001302      488d3d971e20.  lea rdi, [0x002031a0]
            0x00001309      e8f2f6ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x7db
            0x0000130e      be65000000     mov esi, 0x65               ; 'e'
            0x00001313      488d3d861e20.  lea rdi, [0x002031a0]
            0x0000131a      e8e1f6ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x7d0
            0x0000131f      90             nop
            0x00001320      5d             pop rbp
            0x00001321      c3             ret
            0x00001322      55             push rbp
            0x00001323      4889e5         mov rbp, rsp
            0x00001326      488d3d4b3e20.  lea rdi, [0x00205178]
            0x0000132d      e8bef6ffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00001332      85c0           test eax, eax
            0x00001334      742d           je 0x1363
            0x00001336      0fb6056a1f20.  movzx eax, byte [0x002032a7] ; [0x2032a7:1]=0
            0x0000133d      3c75           cmp al, 0x75
            0x0000133f      7511           jne 0x1352
            0x00001341      be28000000     mov esi, 0x28               ; '('
            0x00001346      488d3d531e20.  lea rdi, [0x002031a0]
            0x0000134d      e8aef6ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x81f
            0x00001352      be65000000     mov esi, 0x65               ; 'e'
            0x00001357      488d3d421e20.  lea rdi, [0x002031a0]
            0x0000135e      e89df6ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x814
            0x00001363      90             nop
            0x00001364      5d             pop rbp
            0x00001365      c3             ret
            0x00001366      55             push rbp
            0x00001367      4889e5         mov rbp, rsp
            0x0000136a      488d3d0f2c20.  lea rdi, [0x00203f80]
            0x00001371      e87af6ffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00001376      85c0           test eax, eax
            0x00001378      742d           je 0x13a7
            0x0000137a      0fb6050f1f20.  movzx eax, byte [0x00203290] ; [0x203290:1]=0
            0x00001381      3c5f           cmp al, 0x5f
            0x00001383      7511           jne 0x1396
            0x00001385      be11000000     mov esi, 0x11
            0x0000138a      488d3d0f1e20.  lea rdi, [0x002031a0]
            0x00001391      e86af6ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x863
            0x00001396      be65000000     mov esi, 0x65               ; 'e'
            0x0000139b      488d3dfe1d20.  lea rdi, [0x002031a0]
            0x000013a2      e859f6ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x858
            0x000013a7      90             nop
            0x000013a8      5d             pop rbp
            0x000013a9      c3             ret
            0x000013aa      55             push rbp
            0x000013ab      4889e5         mov rbp, rsp
            0x000013ae      488d3d6b3b20.  lea rdi, [0x00204f20]
            0x000013b5      e836f6ffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x000013ba      85c0           test eax, eax
            0x000013bc      742d           je 0x13eb
            0x000013be      0fb605df1e20.  movzx eax, byte [0x002032a4] ; [0x2032a4:1]=0
            0x000013c5      3c31           cmp al, 0x31
            0x000013c7      7511           jne 0x13da
            0x000013c9      be25000000     mov esi, 0x25               ; '%'
            0x000013ce      488d3dcb1d20.  lea rdi, [0x002031a0]
            0x000013d5      e826f6ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x8a7
            0x000013da      be65000000     mov esi, 0x65               ; 'e'
            0x000013df      488d3dba1d20.  lea rdi, [0x002031a0]
            0x000013e6      e815f6ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x89c
            0x000013eb      90             nop
            0x000013ec      5d             pop rbp
            0x000013ed      c3             ret
            0x000013ee      55             push rbp
            0x000013ef      4889e5         mov rbp, rsp
            0x000013f2      488d3d773620.  lea rdi, [0x00204a70]
            0x000013f9      e8f2f5ffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x000013fe      85c0           test eax, eax
            0x00001400      742d           je 0x142f
            0x00001402      0fb605951e20.  movzx eax, byte [0x0020329e] ; [0x20329e:1]=0
            0x00001409      3c33           cmp al, 0x33
            0x0000140b      7511           jne 0x141e
            0x0000140d      be1f000000     mov esi, 0x1f
            0x00001412      488d3d871d20.  lea rdi, [0x002031a0]
            0x00001419      e8e2f5ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x8eb
            0x0000141e      be65000000     mov esi, 0x65               ; 'e'
            0x00001423      488d3d761d20.  lea rdi, [0x002031a0]
            0x0000142a      e8d1f5ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x8e0
            0x0000142f      90             nop
            0x00001430      5d             pop rbp
            0x00001431      c3             ret
            0x00001432      55             push rbp
            0x00001433      4889e5         mov rbp, rsp
            0x00001436      488d3d7b2a20.  lea rdi, [0x00203eb8]
            0x0000143d      e8aef5ffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00001442      85c0           test eax, eax
            0x00001444      742d           je 0x1473
            0x00001446      0fb605421e20.  movzx eax, byte [0x0020328f] ; [0x20328f:1]=0
            0x0000144d      3c75           cmp al, 0x75
            0x0000144f      7511           jne 0x1462
            0x00001451      be10000000     mov esi, 0x10
            0x00001456      488d3d431d20.  lea rdi, [0x002031a0]
            0x0000145d      e89ef5ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x92f
            0x00001462      be65000000     mov esi, 0x65               ; 'e'
            0x00001467      488d3d321d20.  lea rdi, [0x002031a0]
            0x0000146e      e88df5ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x924
            0x00001473      90             nop
            0x00001474      5d             pop rbp
            0x00001475      c3             ret
            0x00001476      55             push rbp
            0x00001477      4889e5         mov rbp, rsp
            0x0000147a      488d3dbf2420.  lea rdi, [0x00203940]
            0x00001481      e86af5ffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00001486      85c0           test eax, eax
            0x00001488      742d           je 0x14b7
            0x0000148a      0fb605f71d20.  movzx eax, byte [0x00203288] ; [0x203288:1]=0
            0x00001491      3c31           cmp al, 0x31
            0x00001493      7511           jne 0x14a6
            0x00001495      be09000000     mov esi, 9
            0x0000149a      488d3dff1c20.  lea rdi, [0x002031a0]
            0x000014a1      e85af5ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x973
            0x000014a6      be65000000     mov esi, 0x65               ; 'e'
            0x000014ab      488d3dee1c20.  lea rdi, [0x002031a0]
            0x000014b2      e849f5ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x968
            0x000014b7      90             nop
            0x000014b8      5d             pop rbp
            0x000014b9      c3             ret
            0x000014ba      55             push rbp
            0x000014bb      4889e5         mov rbp, rsp
            0x000014be      488d3d132d20.  lea rdi, [0x002041d8]
            0x000014c5      e826f5ffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x000014ca      85c0           test eax, eax
            0x000014cc      742d           je 0x14fb
            0x000014ce      0fb605be1d20.  movzx eax, byte [0x00203293] ; [0x203293:1]=0
            0x000014d5      3c33           cmp al, 0x33
            0x000014d7      7511           jne 0x14ea
            0x000014d9      be14000000     mov esi, 0x14
            0x000014de      488d3dbb1c20.  lea rdi, [0x002031a0]
            0x000014e5      e816f5ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x9b7
            0x000014ea      be65000000     mov esi, 0x65               ; 'e'
            0x000014ef      488d3daa1c20.  lea rdi, [0x002031a0]
            0x000014f6      e805f5ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x9ac
            0x000014fb      90             nop
            0x000014fc      5d             pop rbp
            0x000014fd      c3             ret
            0x000014fe      55             push rbp
            0x000014ff      4889e5         mov rbp, rsp
            0x00001502      488d3d6f2320.  lea rdi, [0x00203878]
            0x00001509      e8e2f4ffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x0000150e      85c0           test eax, eax
            0x00001510      742d           je 0x153f
            0x00001512      0fb6056e1d20.  movzx eax, byte [0x00203287] ; [0x203287:1]=0
            0x00001519      3c70           cmp al, 0x70
            0x0000151b      7511           jne 0x152e
            0x0000151d      be08000000     mov esi, 8
            0x00001522      488d3d771c20.  lea rdi, [0x002031a0]
            0x00001529      e8d2f4ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x9fb
            0x0000152e      be65000000     mov esi, 0x65               ; 'e'
            0x00001533      488d3d661c20.  lea rdi, [0x002031a0]
            0x0000153a      e8c1f4ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0x9f0
            0x0000153f      90             nop
            0x00001540      5d             pop rbp
            0x00001541      c3             ret
            0x00001542      55             push rbp
            0x00001543      4889e5         mov rbp, rsp
            0x00001546      488d3d632220.  lea rdi, [0x002037b0]
            0x0000154d      e89ef4ffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00001552      85c0           test eax, eax
            0x00001554      742d           je 0x1583
            0x00001556      0fb605291d20.  movzx eax, byte [0x00203286] ; [0x203286:1]=0
            0x0000155d      3c6d           cmp al, 0x6d
            0x0000155f      7511           jne 0x1572
            0x00001561      be07000000     mov esi, 7
            0x00001566      488d3d331c20.  lea rdi, [0x002031a0]
            0x0000156d      e88ef4ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0xa3f
            0x00001572      be65000000     mov esi, 0x65               ; 'e'
            0x00001577      488d3d221c20.  lea rdi, [0x002031a0]
            0x0000157e      e87df4ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0xa34
            0x00001583      90             nop
            0x00001584      5d             pop rbp
            0x00001585      c3             ret
            0x00001586      55             push rbp
            0x00001587      4889e5         mov rbp, rsp
            0x0000158a      488d3dd72d20.  lea rdi, [0x00204368]
            0x00001591      e85af4ffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00001596      85c0           test eax, eax
            0x00001598      742d           je 0x15c7
            0x0000159a      0fb605f41c20.  movzx eax, byte [0x00203295] ; [0x203295:1]=0
            0x000015a1      3c73           cmp al, 0x73
            0x000015a3      7511           jne 0x15b6
            0x000015a5      be16000000     mov esi, 0x16
            0x000015aa      488d3def1b20.  lea rdi, [0x002031a0]
            0x000015b1      e84af4ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0xa83
            0x000015b6      be65000000     mov esi, 0x65               ; 'e'
            0x000015bb      488d3dde1b20.  lea rdi, [0x002031a0]
            0x000015c2      e839f4ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0xa78
            0x000015c7      90             nop
            0x000015c8      5d             pop rbp
            0x000015c9      c3             ret
            0x000015ca      55             push rbp
            0x000015cb      4889e5         mov rbp, rsp
            0x000015ce      488d3d633520.  lea rdi, [0x00204b38]
            0x000015d5      e816f4ffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x000015da      85c0           test eax, eax
            0x000015dc      742d           je 0x160b
            0x000015de      0fb605ba1c20.  movzx eax, byte [0x0020329f] ; [0x20329f:1]=0
            0x000015e5      3c5f           cmp al, 0x5f
            0x000015e7      7511           jne 0x15fa
            0x000015e9      be20000000     mov esi, 0x20               ; "@"
            0x000015ee      488d3dab1b20.  lea rdi, [0x002031a0]
            0x000015f5      e806f4ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0xac7
            0x000015fa      be65000000     mov esi, 0x65               ; 'e'
            0x000015ff      488d3d9a1b20.  lea rdi, [0x002031a0]
            0x00001606      e8f5f3ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0xabc
            0x0000160b      90             nop
            0x0000160c      5d             pop rbp
            0x0000160d      c3             ret
            0x0000160e      55             push rbp
            0x0000160f      4889e5         mov rbp, rsp
            0x00001612      488d3d2f2a20.  lea rdi, [0x00204048]
            0x00001619      e8d2f3ffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x0000161e      85c0           test eax, eax
            0x00001620      742d           je 0x164f
            0x00001622      0fb605681c20.  movzx eax, byte [0x00203291] ; [0x203291:1]=0
            0x00001629      3c74           cmp al, 0x74
            0x0000162b      7511           jne 0x163e
            0x0000162d      be12000000     mov esi, 0x12
            0x00001632      488d3d671b20.  lea rdi, [0x002031a0]
            0x00001639      e8c2f3ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0xb0b
            0x0000163e      be65000000     mov esi, 0x65               ; 'e'
            0x00001643      488d3d561b20.  lea rdi, [0x002031a0]
            0x0000164a      e8b1f3ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0xb00
            0x0000164f      90             nop
            0x00001650      5d             pop rbp
            0x00001651      c3             ret
            0x00001652      55             push rbp
            0x00001653      4889e5         mov rbp, rsp
            0x00001656      488d3d733d20.  lea rdi, [0x002053d0]
            0x0000165d      e88ef3ffff     call sym.imp._setjmp        ; int setjmp(jmpbuf env)
            0x00001662      85c0           test eax, eax
            0x00001664      742d           je 0x1693
            0x00001666      0fb6053d1c20.  movzx eax, byte [0x002032aa] ; [0x2032aa:1]=0
            0x0000166d      3c7d           cmp al, 0x7d
            0x0000166f      7511           jne 0x1682
            0x00001671      be64000000     mov esi, 0x64               ; 'd'
            0x00001676      488d3d231b20.  lea rdi, [0x002031a0]
            0x0000167d      e87ef3ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0xb4f
            0x00001682      be65000000     mov esi, 0x65               ; 'e'
            0x00001687      488d3d121b20.  lea rdi, [0x002031a0]
            0x0000168e      e86df3ffff     call sym.imp.longjmp        ; void longjmp(jmp_buf env, int val)
            ; CODE XREF from entry.init0 @ +0xb44
            0x00001693      90             nop
            0x00001694      5d             pop rbp
            0x00001695      c3             ret
```
