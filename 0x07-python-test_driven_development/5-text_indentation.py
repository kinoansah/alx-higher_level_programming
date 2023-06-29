#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_chars = ['.', '?', ':']
    result = ""
    for char in text:
        result += char
        if char in punctuation_chars:
            result += '\n\n'
    print(result.strip())
