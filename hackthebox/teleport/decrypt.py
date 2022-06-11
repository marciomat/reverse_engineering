#!/usr/bin/env python

OFFSET = 2110080  # offset address from first char
passw_dict = {}

# Read input file
with open('movzx.txt') as f:
    lines = f.readlines()

# Create dictionary since chars are not in order
for i in range(0, 86, 2):
    index = int(lines[i], 16) - OFFSET
    passw_chr = chr(int(lines[i+1],16))
    passw_dict[index] = passw_chr

# Print each char in the correct order
for i in range(0, 43):
    print(passw_dict[i], end="")
