#!/usr/bin/python3
c = 0
for i in range(ord('z'), ord('a') - 1, -1):
    print(chr(i).upper( ) if i % 2 == 0 else chr(i).lower( ), end='')
    c = 32 if c == 0 else 0
