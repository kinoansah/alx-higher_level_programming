#!/usr/bin/python3
for tens in range(10):
    for ones in range(tens + 1, 10):
        print("{:01d}{:01d}".format(tens, ones), end="")
        if tens != 8 or ones != 9:
            print(", ", end="")
        else:
            print()
