#!/usr/bin/python3
def print_alphabet(letter='A'):
    if ord(letter) <= ord('Z'):
        print(letter)
        print_alphabet(chr(ord(letter) + 1))

print_alphabet()
