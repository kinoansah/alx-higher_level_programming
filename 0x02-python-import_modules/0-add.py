#!/usr/bin/python3
a = 1
b = 2

add_0 = __import__('add_0').add
result = add_0(a, b)

print(f"{a} + {b} = {result}")
