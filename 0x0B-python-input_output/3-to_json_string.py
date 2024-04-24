#!/usr/bin/python3
""" To JSON string """
import json


def to_json_string(my_object):
    """
    function that returns the JSON representation of an object.

    Args:
        my_object: object to serialize.

    Return:
        Serialized object.
    """
    return json.dumps(my_object)
