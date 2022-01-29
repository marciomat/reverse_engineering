#!/usr/bin/env python3

LAST_CHAR = '~'
FIRST_CHAR = '!'

# Init list of 64 chars with first printable ASCII char for every position
passw_list = ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", 
              "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", 
              "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", 
              "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4"]


magic_str = [0x3a, 0x7e, 0x28, 0x37, 0x35, 0x34, 0x2d, 0x38, 0x6a, 0x6b, 0x73, 0x72, 0x36, 0x34, 0x47, 0x64]

def init_xor(xmm0):
    xmm0_xor = []
    for xmm0_chr, magic_chr in zip(xmm0, magic_str):
        xmm0_xor.append(ord(xmm0_chr) ^ magic_chr)
    return xmm0_xor

def stage_1(xmm0_xor):
    eax = 0x0
    for r8 in reversed(xmm0_xor):
        eax = r8 ^ eax

    return eax

def stage_2(xmm0_xor, xmm1):
    rax = 0x22
    r8 = xmm0_xor[4]
    rax = rax * r8
    rax *= 4
    rax += 0x13a

    rbx = 0
    for xmm1_chr in xmm1:
        rax = rax - ord(xmm1_chr)
        
    return rax


def next_passw_xmm0():
    for i in reversed(range(16)):
        if (passw_list[i] == LAST_CHAR):
            passw_list[i] = FIRST_CHAR
        else:
            passw_list[i] = chr(ord(passw_list[i]) + 1)  # increment to the next char
            break

def next_passw_xmm1():
    for i in reversed(range(16, 32)):
        if (passw_list[i] == LAST_CHAR):
            passw_list[i] = FIRST_CHAR
        else:
            passw_list[i] = chr(ord(passw_list[i]) + 1)  # increment to the next char
            break

# Return password section associated with xmm0
def get_xmm0(passw_list):
    xmm0 = passw_list[:16]
    xmm0.reverse()
    return xmm0

# Return password section associated with xmm1
def get_xmm1(passw_list):
    xmm1 = passw_list[16:32]
    return xmm1

# Return password section associated with xmm2
def get_xmm2(passw_list):
    xmm2 = passw_list[32:48]
    return xmm2

# Return password section associated with xmm3
def get_xmm3(passw_list):
    xmm3 = passw_list[48:]
    return xmm3

# Prints passw_list as one string
def print_passw():
    for i_char in passw_list:
        print(i_char, end="")

# Brute-force to find a string of chars that will pass stages 1 to 3
while True:
    while True:
        xmm0_xor = init_xor(get_xmm0(passw_list))
        if stage_1(xmm0_xor) == 0:
            break
        else:
            next_passw_xmm0()
    

    # Now that stage_1 is validated, let's
    # try to pass the stage_2
    rax = stage_2(xmm0_xor, get_xmm1(passw_list))
    if rax == 0:
        break
    else:
        next_passw_xmm1()
        next_passw_xmm0()


print("password found:")
print_passw()
