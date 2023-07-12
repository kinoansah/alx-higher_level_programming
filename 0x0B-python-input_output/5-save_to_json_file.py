#!/usr/bin/python3
"""
function that writes an Object to a text file
"""

import json


def save_to_json_file(my_obj, filename):
    """Object to a text file, using a JSON representation"""
    with open(filename, mode="w", encoding="utf-8") as _file:
        _file.write(json.dumps(my_obj))
