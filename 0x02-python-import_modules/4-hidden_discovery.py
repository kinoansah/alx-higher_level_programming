#!/usr/bin/python3
import dis

with open('hidden_4.pyc', 'rb') as file:
    code = file.read()

names = []
instructions = dis.get_instructions(code)
for instruction in instructions:
    if (
        instruction.opname == 'LOAD_CONST'
        and isinstance(instruction.argval, str)
        and not instruction.argval.startswith('__')
    ):
        names.append(instruction.argval)

for name in sorted(names):
    print(name)
