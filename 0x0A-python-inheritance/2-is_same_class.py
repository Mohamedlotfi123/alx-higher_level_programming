#!/usr/bin/python3
""" is_same_class function """


def is_same_class(obj, a_class):
    """
    function the check if the object from the class or not.

    Args:
        obj: the object to check.
        a_class: specifice class.

    Return:
        True if obj is instance of a_class, or
        False otherwise.
    """
    if type(obj) is a_class:
        return True
    return False
