#!/usr/bin/python3
""" Create object from a JSON file """
import json


def load_from_json_file(filename):
    """
    function that creates an Object from a JSON file.

    Args:
        filename: JSON file.
    """
    with open(filename, encoding="utf-8") as my_file:
        return json.loads(my_file.read())
