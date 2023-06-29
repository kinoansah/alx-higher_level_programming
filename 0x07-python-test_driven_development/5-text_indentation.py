#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of ., ? and : characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    Examples:
        >>> text_indentation("Lorem ipsum dolor sit amet. Consectetur adipiscing elit.")
        Lorem ipsum dolor sit amet.
        
        Consectetur adipiscing elit.

        >>> text_indentation("Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere?")
        Quonam modo?
        
        Utrum igitur tibi litteram videor an totas paginas commovere?

        >>> text_indentation("Non autem hoc: igitur ne illud quidem.")
        Non autem hoc:
        
        igitur ne illud quidem.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = [".", "?", ":"]
    result = ""
    for char in text:
        result += char
        if char in chars:
            result += "\n\n"

    print(result.strip())
