#!/usr/bin/python3
import sys

num_args = len(sys.argv) - 1
plural_suffix = "s" if num_args != 1 else ""
arg_str = "argument" + plural_suffix if num_args != 0 else "no arguments"

print(f"Number of argument{plural_suffix}: {num_args}")
print(f"{arg_str}: {'.' if num_args == 0 else ':'}")

for i, arg in enumerate(sys.argv[1:], start=1):
    print(f"{i}: {arg}")
