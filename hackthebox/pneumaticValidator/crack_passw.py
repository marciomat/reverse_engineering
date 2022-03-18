#!/usr/bin/env python3

from string import ascii_letters, digits, punctuation
import r2pipe
import struct
import time


#passw = "00000000000000000000"
#passw = "HT000000000000000000"
#passw = "HTB{000000000000000}"
#passw = "HTB{P00000000000000}"
#passw = "HTB{PN0000000000000}"
#passw = "HTB{PN?000000000000}"
#passw = "HTB{PN?U00000000000}"
#passw = "HTB{PN?Um0000000000}"
#passw = "HTB{PN?Um4000000000}"
#passw = "HTB{PN?Um4t1C_00000}"
#passw = "HTB{PN?Um4t1C_l0g1C}"
#passw = "HTB{PN3Um4t1C_l0g1C}"
passw = "HTB{pN3Um4t1C_l0g1C}"
FIRST_CHR = 4
LAST_CHR = FIRST_CHR + 1


def get_fcn_543c_base_address():
    list_addr = r.cmdj('afij fcn.0000543c')
    base_addr = list_addr[0]['offset']                # get the 1st address that calls fcn.000054e0
    return (base_addr & 0xffffffffff00)

def get_fcn_5498_base_address():
    list_addr = r.cmdj('afij fcn.00005498')
    base_addr = list_addr[0]['offset']                # get the 1st address that calls fcn.000054e0
    return (base_addr & 0xfffffffff000)

def get_fcn_main_base_address():
    list_addr = r.cmdj('afij main')
    base_addr = list_addr[0]['offset']                # get the 1st address that calls fcn.000054e0
    return (base_addr & 0xfffffffff000)

def set_breakpoint(addr):
    r.cmd('db-*')                                   # first remove all breakpoints
    bp_addr = addr                                  # full address for breakpoint
    r.cmd('db ' + str(bp_addr))                     # add breakpoint

def get_passw_array_addr():
    base_addr = get_fcn_543c_base_address()
    instr_address = base_addr | 0x80
    r.cmd('s ' + str(instr_address))
    disasm = r.cmdj('pij 1')
    return (disasm[0]['disasm'][12:24])

def set_bits():
    passw_addr = int(get_passw_array_addr(), 16)
    fcn_addr = get_fcn_5498_base_address()
    set_breakpoint(fcn_addr | 0x4df)
    r.cmd('dc')                                         # run until breakpoint
    for i in range(TOTAL_BITS):
        #bit_addr = passw_addr + (i * 4)
        bit_addr = passw_addr + ((21 + i) * 4)
        #if (binary_passw[i] == 1):
        if (binary_passw_temp[i] == 1):
            r.cmd('wx 01 @ ' + str(bit_addr))
        
    ret = r.cmd('px 100 @ ' + str(passw_addr))
    print(ret)

def get_max_value(new_passw):
        r.cmd('ood ' + new_passw)               # password need 20 chars
        main_base_addr = get_fcn_main_base_address()
        set_breakpoint(main_base_addr | 0x635)
        r.cmd('dc')                                     # run until breakpoint
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
        #for new_char in digits + ascii_letters:
        for new_char in ascii_letters + digits+ punctuation:
        #for new_char in punctuation:
            pw_list[i] = new_char
            print("Trying password: ", "".join(pw_list))
            new_value = get_max_value("".join(pw_list))
            print("new value: ", new_value)
            if new_value == current_value:
                print("****** Equal value for the char: ", new_char, "\n")
            if new_value < current_value:
                best_char = new_char
                current_value = new_value
                print("****** found new best_char: ", best_char, "\n")
        print("-------------------\n")
        pw_list[i] = best_char
        passw = "".join(pw_list)
        print("Password so far: ", passw)

    

### Beginning ###

#r = r2pipe.open('pneumaticvalidator')
r = r2pipe.open('pneumaticvalidator', flags=['-2'])     # -2 signifies disable stderr
r.cmd('aaaa')                                           # radare2 command to analyze the code to find the functions

bruteforce_chars()

#ret = r.cmd('pi 10')
#print(ret)

r.quit()


