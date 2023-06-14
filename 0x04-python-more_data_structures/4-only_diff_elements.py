#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Create an empty set to store the unique elements
    unique_set = set()

    # Iterate over each element in set_1
    for item in set_1:

        if item not in set_2:
            unique_set.add(item)

    # Iterate over each element in set_2
    for item in set_2:

        if item not in set_1:
            unique_set.add(item)

    return unique_set
