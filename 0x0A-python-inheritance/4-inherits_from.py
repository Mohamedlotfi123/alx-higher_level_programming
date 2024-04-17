#!/usr/bin/python3
""" inherits_from function """


def inherits_from(obj, a_class):
    """
    function check if an object is instance of a class that inherited
    from the specified class or not.

    Args:
        obj: the object to check.
        a_class: specifice class.

    Return:
        True if obj is instance of inherited class of a_class,
        or False otherwise.
    """
    if isinstance(obj, a_class) and not type(obj) == a_class:
        return True
    return False
