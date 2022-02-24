#!/usr/bin/env python3

import r2pipe

check_offset = [0x5d15, 0x5d42, 0x5d71, 0x5da0, 0x5dcf, 0x5dfc, 0x5e28, 0x5e55, 0x5e82, 0x5eaf, 0x5edc, 0x5f0c, 0x5f3c, 0x5f6c, 0x5f9c, 0x5fcc, 0x5ffc, 0x602c, 0x605c, 0x608c, 0x60bc, 0x60ec, 0x611c, 0x614c, 0x617c, 0x61ac, 0x61dc, 0x620c, 0x623c, 0x626c, 0x629c, 0x62c8]
expected_byte = [0xe6, 0x1f, 0xf9, 0x74, 0x22, 0x68, 0xf9, 0xc7, 0x8d, 0x22, 0x7b, 0x3a, 0xae, 0x48, 0x31, 0xcb, 0xcb, 0x22, 0x46, 0x5, 0xce, 0x3e, 0xcd, 0x2b, 0x12, 0x20, 0x7b, 0x50, 0x83, 0xb8, 0xcf, 0x7b]
reg_to_check = ['bl', 'bl', 'sil', 'sil', 'sil', 'cl', 'al', 'al', 'al', 'al', 'al', 'al', 'al', 'al', 'al', 'al', 'al', 'al', 'al', 'al', 'al', 'al', 'al', 'al', 'al', 'al', 'al', 'al', 'al', 'al', 'al', 'al']

def get_base_address():
    list_addr = r.cmdj('axtj fcn.000054e0')
    base_addr = list_addr[0]['from']                # get the 1st address that calls fcn.000054e0
    return (base_addr & 0xfffffff00000)

def set_breakpoint(offset_i):
    r.cmd('db-*')                                   # first remove all breakpoints
    base_addr = get_base_address()
    check_addr = base_addr | check_offset[offset_i] # set address for `cmp` instruction
    r.cmd('db ' + str(check_addr))                  # add breakpoint

def crack_check(passw, i_offset):
    print('--------------------')
    r.cmd('ood picoCTF{' + passw + '}')
    set_breakpoint(i_offset)
    
    r.cmd('dc')                                 # run until breakpoint
    result = int(r.cmd('dr ' + reg_to_check[i_offset]), 16)
    print(passw)
    return (result)

def gen_passw(passw, i, char):
    passw_list = list(passw)
    passw_list[i] = char
    return ("".join(passw_list))


r = r2pipe.open('checkpass', flags=['-2']) # -2 signifies disable stderr
r.cmd('aaaa')

final_passw = 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ'  # 32 chars
#final_passw = 'ZZZZZZZZZZZhZZZZZ_ZZZZZZZZZZZZZZ'  # 32 chars
#final_passw = 'ZZZZZZZZZZZhZZZZZ_ZZZZZZ5ZOZZZZZ'  # 32 chars
#final_passw = 'ZZZZZZZZZZZhZZZZZ_ZZeZZZ5ZOZ4ZZZ'  # 32 chars
#final_passw = 'ZZZZZZZZZZZhZZZZZ_ZZeZ5Z5ZOZ4ZZq'  # 32 chars
#final_passw = 'ZZZZZZZZZZZhZZZZZ_ZZeZ5Z5eOZ4Z6q'  # 32 chars
#final_passw = 'ZZZZnZZZZZZhZZZ3Z_ZZeZ5Z5eOZ4Z6q'  # 32 chars
#final_passw = 'ZZmZnZZZZZZhZZZ3l_ZZeZ5Z5eOZ4Z6q'  # 32 chars
#final_passw = 'Z1mZnZZZZZZhZZZ3l_ZWeZ5Z5eOZ4Z6q'  # 32 chars
#final_passw = 'Z1mZnZZ1ZeZhZZZ3l_ZWeZ5Z5eOZ4Z6q'  # 32 chars
#final_passw = 'Z1mZnZS1ZeZhaZZ3l_ZWeZ5Z5eOZ4Z6q'  # 32 chars
#final_passw = 'Z1mZnZS1ZeZhaZZ3l_NWeA5Z5eOZ4Z6q'  # 32 chars
#final_passw = 'Z1minZS1ZeZhaZZ3l_NWeA5Z5eOZ4P6q'  # 32 chars
#final_passw = 't1minZS1ZeZhaZZ3l_NWeA525eOZ4P6q'  # 32 chars
#final_passw = 't1minZS1ZeChaZn3l_NWeA525eOZ4P6q'  # 32 chars
#final_passw = 't1mingS1ZeChaZn3l_NWeA525eOE4P6q'  # 32 chars

#final_passw = 't1mingS1deChann3l_NWeA525eOE4P6q'  # 32 chars
#i_char_cracked = [11, 17, 24, 26, 20, 28, 22, 31, 30, 25, 4, 15, 16, 2, 19, 1, 7, 9, 6, 12, 18, 21, 3, 29, 23, 0, 14, 10, 27, 5, 8, 13]

i_char_cracked = []

for i in range(32):
    print("Searching char to crack:")
    sample = crack_check(final_passw, i)                # first sample to compare later on

    for i_chr in range(len(final_passw)):
        if not(i_chr in i_char_cracked):                # don't modify chars already cracked
            passw = gen_passw(final_passw, i_chr, 'b')  # test password with only one char modified
            if (crack_check(passw, i) != sample):       # compare with sample to see if the change affected the current password check
                break
    
    print("Index of next char to crack: ", i_chr)
    print("Burteforcing char...")
    
    for ch_1 in range(48, 125, 1):                      # iterate chars from '0' to '}'
        passw = gen_passw(final_passw, i_chr, chr(ch_1))
        if crack_check(passw, i) == expected_byte[i]:
            print("Cracked char! So far password is: ", passw)
            break
    
    i_char_cracked.append(i_chr)                        # keep track of chars already cracked
    final_passw = passw                                 # update password to use in the next iteration

print("\n\nFinal Password: ")
print(passw)
