#!/usr/bin/env python3

def get_key(input_var):
    return (len(input_var) * (-10)) + 0x34e7

def add_chars(input_var):
    acc = 0
    for i in input_var:
        acc += ord(i)

    return acc

def automated():
    char = 'Z'  # The higher the ASCII value the shorter the license key
    passwd = char

    while (add_chars(passwd) < get_key(passwd)):    # Add 'Z' char until the sum of ASCII is greater than generated key
        passwd = passwd + char

    found = False
    while (found == False):
        if (get_key(passwd) == add_chars(passwd)):
            found = True
            print("\n\nFound!\n\n")
            return passwd
        else:
            print (passwd)
            print ("Length:", len(passwd))
            print ("key:", (get_key(passwd)))
            print ("sum:", (add_chars(passwd)))
            char = chr(ord(char) - 1)
            passwd = passwd[:-1]  # replaces last char with one with lower ASCII value until get_key(passwd) == add_chars(passwd)
            passwd = passwd + char 


passwd = automated()


print (passwd)
print ("Length:", len(passwd))
print ("key:", (get_key(passwd)))
print ("sum:", (add_chars(passwd)))
