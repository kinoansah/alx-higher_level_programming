#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_nums = set()

    for num in my_list:

        unique_nums.add(num)

    total = sum(unique_nums)

    return total
