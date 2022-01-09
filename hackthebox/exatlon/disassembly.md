```assembly
            ; DATA XREF from entry0 @ 0x4049ad
┌ 460: int main (int argc, char **argv, char **envp);
│           ; var int64_t user_input @ rbp-0x50
│           ; var int64_t encrypted_input @ rbp-0x30
│           0x00404c2c      55             push rbp
│           0x00404c2d      4889e5         mov rbp, rsp
│           0x00404c30      4154           push r12
│           0x00404c32      53             push rbx
│           0x00404c33      4883ec40       sub rsp, 0x40
│           ; CODE XREF from main @ 0x404de5
│       ┌─> 0x00404c37      488d35d16314.  lea rsi, [0x0054b00f]       ; "\n" ; int64_t arg2
│       ╎   0x00404c3e      488d3d3b691a.  lea rdi, obj.std::cout      ; 0x5ab580 ; "@^Z" ; int64_t arg1
│       ╎   0x00404c45      e806380600     call method std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*) ; method.std::basic_ostream_char__std::char_traits_char____std::operator____std.char_traits_char____std::basic_ostream_char__std::char_traits_char_____char_const_
│       ╎   0x00404c4a      488d35c76314.  lea rsi, str.__________________________n ; 0x54b018 ; int64_t arg2
│       ╎   0x00404c51      488d3d28691a.  lea rdi, obj.std::cout      ; 0x5ab580 ; "@^Z" ; int64_t arg1
│       ╎   0x00404c58      e8f3370600     call method std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*) ; method.std::basic_ostream_char__std::char_traits_char____std::operator____std.char_traits_char____std::basic_ostream_char__std::char_traits_char_____char_const_
│       ╎   0x00404c5d      488d35746414.  lea rsi, str.__________________n ; 0x54b0d8 ; int64_t arg2
│       ╎   0x00404c64      488d3d15691a.  lea rdi, obj.std::cout      ; 0x5ab580 ; "@^Z" ; int64_t arg1
│       ╎   0x00404c6b      e8e0370600     call method std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*) ; method.std::basic_ostream_char__std::char_traits_char____std::operator____std.char_traits_char____std::basic_ostream_char__std::char_traits_char_____char_const_
│       ╎   0x00404c70      bf01000000     mov edi, 1                  ; int64_t arg1
│       ╎   0x00404c75      e856541000     call sym.__sleep
│       ╎   0x00404c7a      488d35276514.  lea rsi, str.______________________________n ; 0x54b1a8 ; int64_t arg2
│       ╎   0x00404c81      488d3df8681a.  lea rdi, obj.std::cout      ; 0x5ab580 ; "@^Z" ; int64_t arg1
│       ╎   0x00404c88      e8c3370600     call method std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*) ; method.std::basic_ostream_char__std::char_traits_char____std::operator____std.char_traits_char____std::basic_ostream_char__std::char_traits_char_____char_const_
│       ╎   0x00404c8d      488d35cc6514.  lea rsi, str.____________________________n ; 0x54b260 ; int64_t arg2
│       ╎   0x00404c94      488d3de5681a.  lea rdi, obj.std::cout      ; 0x5ab580 ; "@^Z" ; int64_t arg1
│       ╎   0x00404c9b      e8b0370600     call method std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*) ; method.std::basic_ostream_char__std::char_traits_char____std::operator____std.char_traits_char____std::basic_ostream_char__std::char_traits_char_____char_const_
│       ╎   0x00404ca0      bf01000000     mov edi, 1                  ; int64_t arg1
│       ╎   0x00404ca5      e826541000     call sym.__sleep
│       ╎   0x00404caa      488d356f6614.  lea rsi, str._____________n ; 0x54b320 ; int64_t arg2
│       ╎   0x00404cb1      488d3dc8681a.  lea rdi, obj.std::cout      ; 0x5ab580 ; "@^Z" ; int64_t arg1
│       ╎   0x00404cb8      e893370600     call method std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*) ; method.std::basic_ostream_char__std::char_traits_char____std::operator____std.char_traits_char____std::basic_ostream_char__std::char_traits_char_____char_const_
│       ╎   0x00404cbd      bf01000000     mov edi, 1                  ; int64_t arg1
│       ╎   0x00404cc2      e809541000     call sym.__sleep
│       ╎   0x00404cc7      488d35326714.  lea rsi, str.___________________n_n_n ; 0x54b400 ; int64_t arg2
│       ╎   0x00404cce      488d3dab681a.  lea rdi, obj.std::cout      ; 0x5ab580 ; "@^Z" ; int64_t arg1
│       ╎   0x00404cd5      e876370600     call method std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*) ; method.std::basic_ostream_char__std::char_traits_char____std::operator____std.char_traits_char____std::basic_ostream_char__std::char_traits_char_____char_const_
│       ╎   0x00404cda      bf01000000     mov edi, 1                  ; int64_t arg1
│       ╎   0x00404cdf      e8ec531000     call sym.__sleep
│       ╎   0x00404ce4      488d45b0       lea rax, [user_input]
│       ╎   0x00404ce8      4889c7         mov rdi, rax                ; int64_t arg1
│       ╎   0x00404ceb      e840850600     call fcn.0046d230
│       ╎   0x00404cf0      488d35d96714.  lea rsi, str.___Enter_Exatlon_Password__:_ ; 0x54b4d0 ; "[+] Enter Exatlon Password  : " ; int64_t arg2
│       ╎   0x00404cf7      488d3d82681a.  lea rdi, obj.std::cout      ; 0x5ab580 ; "@^Z" ; int64_t arg1
│       ╎   0x00404cfe      e84d370600     call method std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*) ; method.std::basic_ostream_char__std::char_traits_char____std::operator____std.char_traits_char____std::basic_ostream_char__std::char_traits_char_____char_const_
│       ╎   0x00404d03      488d45b0       lea rax, [user_input]
│       ╎   0x00404d07      4889c6         mov rsi, rax
│       ╎   0x00404d0a      488d3d8f691a.  lea rdi, obj.std::cin       ; 0x5ab6a0
│       ╎   0x00404d11      e87a200000     call method std::basic_istream<char, std::char_traits<char> >& std::operator>><char, std::char_traits<char>, std::allocator<char> >(std::basic_istream<char, std::char_traits<char> >&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&) ; method.std::basic_istream_char__std::char_traits_char____std::operator___char__std::char_traits_char___std.allocator_char____std::basic_istream_char__std::char_traits_char_____std::__cxx11::basic_string_char__std::char_traits_char___std::allocator_char
│       ╎   0x00404d16      488d45d0       lea rax, [encrypted_input]
│       ╎   0x00404d1a      488d55b0       lea rdx, [user_input]
│       ╎   0x00404d1e b    4889d6         mov rsi, rdx                ; int64_t arg2
│       ╎   0x00404d21      4889c7         mov rdi, rax                ; int64_t arg1
│       ╎   0x00404d24      e884fdffff     call sym exatlon(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) ; sym.exatlon_std::__cxx11::basic_string_char__std::char_traits_char___std::allocator_char____const_
│       ╎   0x00404d29      488d45d0       lea rax, [encrypted_input]
│       ╎   0x00404d2d b    488d35bc6714.  lea rsi, str.1152_1344_1056_1968_1728_816_1648_784_1584_816_1728_1520_1840_1664_784_1632_1856_1520_1728_816_1632_1856_1520_784_1760_1840_1824_816_1584_1856_784_1776_1760_528_528_2000_ ; 0x54b4f0 ; "1152 1344 1056 1968 1728 816 1648 784 1584 816 1728 1520 1840 1664 784 1632 1856 1520 1728 816 1632 1856 1520 784 1760 1840 1824 816 1584 1856 784 1776 1760 528 528 2000 " ; int64_t arg2
│       ╎   0x00404d34      4889c7         mov rdi, rax                ; int64_t arg1
│       ╎   0x00404d37      e8be030000     call method bool std::operator==<char, std::char_traits<char>, std::allocator<char> >(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, char const*) ; method.bool_std::operator_char__std::char_traits_char___std.allocator_char____std::__cxx11::basic_string_char__std::char_traits_char___std::allocator_char____const__char_const_
│       ╎   0x00404d3c      89c3           mov ebx, eax
│       ╎   0x00404d3e      488d45d0       lea rax, [encrypted_input]
│       ╎   0x00404d42      4889c7         mov rdi, rax                ; uint32_t arg1
│       ╎   0x00404d45      e8e6850600     call method std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::~basic_string() ; method.std::__cxx11::basic_string_char__std::char_traits_char___std::allocator_char___.basic_string__
│       ╎   ;-- rip:
│       ╎   0x00404d4a      84db           test bl, bl
│      ┌──< 0x00404d4c      7435           je 0x404d83
│      │╎   0x00404d4e      488d35466814.  lea rsi, str.___Looks_Good____n_n_n ; 0x54b59b ; "[+] Looks Good ^_^ \n\n\n" ; int64_t arg2
│      │╎   0x00404d55      488d3d24681a.  lea rdi, obj.std::cout      ; 0x5ab580 ; "@^Z" ; int64_t arg1
│      │╎   0x00404d5c      e8ef360600     call method std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*) ; method.std::basic_ostream_char__std::char_traits_char____std::operator____std.char_traits_char____std::basic_ostream_char__std::char_traits_char_____char_const_
│      │╎   0x00404d61      4889c2         mov rdx, rax
│      │╎   0x00404d64      48c7c0207e46.  mov rax, method.std::basic_ostream_char__std::char_traits_char____std::endl_char__std.char_traits_char____std::basic_ostream_char__std::char_traits_char____ ; 0x467e20 ; "ATUH\x83\xec\bH\x8b\aH\x8b@\xe8L\x8b\xa4\a\xf0"
│      │╎   0x00404d6b      4889c6         mov rsi, rax
│      │╎   0x00404d6e      4889d7         mov rdi, rdx                ; int64_t arg2
│      │╎   0x00404d71      e87a240600     call method std::ostream::operator<<(std::ostream& (*)(std::ostream&)) ; method.std::ostream.operator___std::ostream____std::ostream__
│      │╎   0x00404d76      41bc00000000   mov r12d, 0
│      │╎   0x00404d7c      bb00000000     mov ebx, 0
│     ┌───< 0x00404d81      eb51           jmp 0x404dd4
│     ││╎   ; CODE XREF from main @ 0x404d4c
│     │└──> 0x00404d83      488d45b0       lea rax, [user_input]
│     │ ╎   0x00404d87      488d35246814.  lea rsi, [0x0054b5b2]       ; "q" ; int64_t arg2
│     │ ╎   0x00404d8e      4889c7         mov rdi, rax                ; int64_t arg1
│     │ ╎   0x00404d91      e864030000     call method bool std::operator==<char, std::char_traits<char>, std::allocator<char> >(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, char const*) ; method.bool_std::operator_char__std::char_traits_char___std.allocator_char____std::__cxx11::basic_string_char__std::char_traits_char___std::allocator_char____const__char_const_
│     │ ╎   0x00404d96      84c0           test al, al
│     │┌──< 0x00404d98      740d           je 0x404da7
│     ││╎   0x00404d9a      41bc00000000   mov r12d, 0
│     ││╎   0x00404da0      bb00000000     mov ebx, 0
│    ┌────< 0x00404da5      eb2d           jmp 0x404dd4
│    │││╎   ; CODE XREF from main @ 0x404d98
│    ││└──> 0x00404da7      488d35066814.  lea rsi, str._______n       ; 0x54b5b4 ; "[-] ;(\n" ; int64_t arg2
│    ││ ╎   0x00404dae      488d3dcb671a.  lea rdi, obj.std::cout      ; 0x5ab580 ; "@^Z" ; int64_t arg1
│    ││ ╎   0x00404db5      e896360600     call method std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*) ; method.std::basic_ostream_char__std::char_traits_char____std::operator____std.char_traits_char____std::basic_ostream_char__std::char_traits_char_____char_const_
│    ││ ╎   0x00404dba      4889c2         mov rdx, rax
│    ││ ╎   0x00404dbd      48c7c0207e46.  mov rax, method.std::basic_ostream_char__std::char_traits_char____std::endl_char__std.char_traits_char____std::basic_ostream_char__std::char_traits_char____ ; 0x467e20 ; "ATUH\x83\xec\bH\x8b\aH\x8b@\xe8L\x8b\xa4\a\xf0"
│    ││ ╎   0x00404dc4      4889c6         mov rsi, rax
│    ││ ╎   0x00404dc7      4889d7         mov rdi, rdx                ; int64_t arg2
│    ││ ╎   0x00404dca      e821240600     call method std::ostream::operator<<(std::ostream& (*)(std::ostream&)) ; method.std::ostream.operator___std::ostream____std::ostream__
│    ││ ╎   0x00404dcf      bb01000000     mov ebx, 1
│    ││ ╎   ; CODE XREFS from main @ 0x404d81, 0x404da5
│    └└───> 0x00404dd4      488d45b0       lea rax, [user_input]
│       ╎   0x00404dd8      4889c7         mov rdi, rax                ; uint32_t arg1
│       ╎   0x00404ddb      e850850600     call method std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::~basic_string() ; method.std::__cxx11::basic_string_char__std::char_traits_char___std::allocator_char___.basic_string__
│       ╎   0x00404de0      83fb01         cmp ebx, 1                  ; rdi
│      ┌──< 0x00404de3      7505           jne 0x404dea
│      │└─< 0x00404de5      e94dfeffff     jmp 0x404c37
│      │    ; CODE XREF from main @ 0x404de3
│      └──> 0x00404dea      4489e0         mov eax, r12d
│       ┌─< 0x00404ded      eb1a           jmp 0x404e09
..
│       │   ; CODE XREF from main @ 0x404ded
│       └─> 0x00404e09      4883c440       add rsp, 0x40
│           0x00404e0d      5b             pop rbx
│           0x00404e0e      415c           pop r12
│           0x00404e10      5d             pop rbp
└           0x00404e11      c3             ret
```