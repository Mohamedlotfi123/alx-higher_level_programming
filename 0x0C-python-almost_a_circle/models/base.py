#!/usr/bin/python3
""" Base Class """


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
