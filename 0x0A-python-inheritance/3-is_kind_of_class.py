#!/usr/bin/python3
""" is_same_class function """


def is_kind_of_class(obj, a_class):
    """
    function check if the object is an instance of
    the class or a class that inherited from.

    Args:
        obj: the object to check.
        a_class: specifice class.

    Return:
        True if obj is instance of a_class or a class inherited from,
        or False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
