#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    function that executes a function safely.

    Args:
        fct: function pointer.
        args: argument to the function.

    Return:
        Result of the function, or otherwise None.
    """
    try:
        return fct(*args)
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
