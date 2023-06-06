#!/usr/bin/python3
def reverse_alphabet():
    for i in range(25, -1, -1):
        if i % 2 == 0:
            print(f"{chr(97 + i)}{chr(65 + i)}", end=" ")
        else:
            print(f"{chr(65 + i)}{chr(97 + i)}", end=" ")

reverse_alphabet()

