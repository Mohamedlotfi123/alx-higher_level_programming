#!/usr/bin/python3
""" say_my_name function """


def say_my_name(first_name, last_name=""):
    """
    function that prints "My name is <first_name> <last_name>"

    Args:
        first_name: first name of anyone.
        last_name: last name of anyone.

    Raise:
        TypeError: if first_name or last_name is not string.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
