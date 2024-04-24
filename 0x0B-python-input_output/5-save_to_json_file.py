#!/usr/bin/python3
""" Save object to a file. """
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an object to a text file using JSON representation.

    Args:
        my_obj: object to save.
        filename: name of the file to save in.
    """
    with open(filename, "a", encoding="utf-8") as my_file:
        my_file.write(json.dumps(my_obj))
