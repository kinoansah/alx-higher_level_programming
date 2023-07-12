#!/usr/bin/python3
"""This module defines a Rectangle subclass Square"""
from 9-rectangle import Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size):
        """Initialize a new square"""
        super().__init__(size, size)
        self.__size = size
