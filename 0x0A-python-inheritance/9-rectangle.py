#!/usr/bin/python3

"""Rectangle Module."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class."""

    def __init__(self, width, height):
        """Initialize the rectangle class."""
        self.integer_validator( 'width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """A method that returns the rectangle area."""
        return self.__width = self.__height

    def __str__(self) -> str:
        """A method that creates a string object from a given object"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
