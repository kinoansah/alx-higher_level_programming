#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    # Variable to keep track of the printed elements
    printed_elements = 0

    try:
        # Print the elements
        for i in range(x):
            print(my_list[i], end=" ") # Print element followed by a space
            printed_elements += 1 # Increment the counter

        # Print a new line
        print()

    except IndexError:
        # If an IndexError occurs, it means that all elements have been printed
        pass

    return printed_elements
