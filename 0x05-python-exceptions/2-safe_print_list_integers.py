#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0

    try:
        # Print the integers
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                printed_integers += 1   # Increment the counter

    except IndexError:
        # If an IndexError occurs, it means
        # that all elements have been accessed
        pass

    finally:
        print()  # Print a new line after all elements

        return printed_integers
