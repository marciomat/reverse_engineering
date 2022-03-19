#!/usr/bin/env python3

from string import ascii_letters, digits, punctuation
import r2pipe
import struct

#passw = "00000000000000000000"
#passw = "HTB{PN?Um4t1C_l0g1C}"
#passw = "HTB{PN3Um4t1C_l0g1C}"
passw = "HTB{pN3Um4t1C_l0g1C}"
FIRST_CHR = 4
LAST_CHR = 5


def get_fcn_main_base_address():
    list_addr = r.cmdj('afij main')
    base_addr = list_addr[0]['offset']
    return (base_addr & 0xfffffffff000)

def set_breakpoint(addr):
    r.cmd('db-*')                                   # first remove all breakpoints
    bp_addr = addr
    r.cmd('db ' + str(bp_addr))                     # add breakpoint


def get_max_value(new_passw):
        r.cmd('ood ' + new_passw)                   # reload binary
        main_base_addr = get_fcn_main_base_address()
        set_breakpoint(main_base_addr | 0x635)
        r.cmd('dc')                                 # run until breakpoint
        new_value_hex = hex(int(r.cmd('dr eax')[2:], 16))
        new_value_str = str(new_value_hex)[2:]
        new_value_float = struct.unpack('!f', bytes.fromhex(new_value_str))[0]
        return new_value_float


def bruteforce_chars():
    global passw
    pw_list = list(passw)

    for i in range(FIRST_CHR, LAST_CHR):
        current_value = get_max_value("".join(pw_list))
        print("current value: ", current_value)
        best_char = '0'
        for new_char in ascii_letters + digits+ punctuation:
            pw_list[i] = new_char
            print("Trying password: ", "".join(pw_list))
            new_value = get_max_value("".join(pw_list))
            print("new value: ", new_value)

            if new_value < current_value:           # found a better solution
                best_char = new_char
                current_value = new_value
                print("****** found new best_char: ", best_char, "\n")

        print("-------------------\n")
        pw_list[i] = best_char
        passw = "".join(pw_list)
        print("Password so far: ", passw)

    

### Beginning ###

r = r2pipe.open('pneumaticvalidator', flags=['-2'])     # -2 signifies disable stderr
r.cmd('aaaa')                                           # radare2 command to analyze the code to find the functions

bruteforce_chars()

r.quit()
