#!/usr/bin/python3
""" Base Class """
import json


class Base():
    """
    Base class.

    Attributes:
        class:
            __nb_objects: ...
        instance:
            id: id of the instance.
    methods:
        __init__: initialization method.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialization method.

        Args:
            id: id of the instance.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        function that returns JSON representation of list_dictionaries.

        Args:
            list_dictionaries: list of dictionaries.

        Return:
            JSON representation of list_dictionaries, or
                "[]" if list_dictionaries is None.
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
