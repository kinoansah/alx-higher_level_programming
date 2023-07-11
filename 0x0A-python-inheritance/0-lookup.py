#!/usr/bin/python3
"""This program returns a list with the methods of an obj"""


def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    return dir(obj)
