#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
    function that prints the first x elements of a list
    and only integers.

    Args:
        my_list: list contain any type.
        x: number of element can access in my_list.
    Return:
        real number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except TypeError:
            continue
        except ValueError:
            continue
    print("")
    return count
