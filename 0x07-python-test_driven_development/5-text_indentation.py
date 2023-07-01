#!/usr/bin/python3
"""
This module contains one function
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = [".", "?", ":"]
    new_text = text.strip()
    for delimiter in delimiters:
        new_text = new_text.replace(delimiter, delimiter + "\n\n")

    print(new_text)
