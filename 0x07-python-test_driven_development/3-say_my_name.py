#!/usr/bin/python3
"""
This module contains one function called 'say_my_name'
"""


def say_my_name(first_name, last_name=""):
    """Function prints "My name is <first_name> <last_name>"."""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
