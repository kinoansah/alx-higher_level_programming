#!/usr/bin/python3
a = 10
b = 5

from calculator_1 import add, subtract, multiply, divide

addition_result = add(a, b)
subtraction_result = subtract(a, b)
multiplication_result = multiply(a, b)
division_result = divide(a, b)

print(f"{a} + {b} = {addition_result}")
print(f"{a} - {b} = {subtraction_result}")
print(f"{a} * {b} = {multiplication_result}")
print(f"{a} / {b} = {division_result}")
