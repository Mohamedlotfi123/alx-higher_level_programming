#!/usr/bin/python3


def safe_print_division(a, b):
    """
    funcion that divides 2 integers and prints the result.

    Args:
        a: first number.
        b: second number.

    Return:
        the division result, or otherwise None.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
