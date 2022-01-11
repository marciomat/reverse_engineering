#!/usr/bin/env python3

# Each of the encoded chars are subtracted by 0x20
def print_char(char):
    print(chr(char + 0x20), end="")


# Encrypted password found in the memory
encr_passw = [0x5d, 0x10, 0x14, 0x4c, 0x43, 0x10, 0x43, 0x4e, 0x4d, 0x14, 0x3f, 0x47, 0x4c, 0x34, 0x23, 0x26, 0x41, 0x5b, 0x28, 0x52, 0x10, 0x11, 0x3f, 0x53, 0x11, 0x4c, 0x54, 0x52]
half_i = len(encr_passw) // 2


# First char is the one in the middle
print_char(encr_passw[half_i])

# The following chars alternate going further from the middle 
for i in range(1, half_i):
    print_char(encr_passw[half_i - i])
    print_char(encr_passw[half_i + i])

# Last char is in the first position (furthest from the midle)
print_char(encr_passw[0])
