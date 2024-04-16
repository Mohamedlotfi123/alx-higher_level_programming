#!/usr/bin/python3
" Lookup function "


def lookup(obj):
    """ Function that return a list of all available attributes and methods
        of an object.

        Args:
            obj: an object to list it's attributes and methods.

        Return:
            list of all available attributes and methods of the object.
        """
    return list(dir(obj))
