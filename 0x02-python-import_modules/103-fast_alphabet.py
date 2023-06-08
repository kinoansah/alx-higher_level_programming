#!/usr/bin/python3
def print_alphabet(index=65):
    print(chr(index))
    if index < 90:
        print_alphabet(index + 1)


print_alphabet()
