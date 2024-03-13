#!/usr/bin/python3


def print_last_digit(number):
    """
    Function that prints the last digit of a number.

    Args:
        number: number to print it's last digit

    Return:
        The last digit of a number
    """
    if number < 0:
        number = -1 * number
    print(number % 10, end="")
    return (number % 10)
