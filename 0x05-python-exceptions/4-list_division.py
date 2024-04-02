#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
    function that divides element by element 2 lists.

    Args:
        my_list_1: list contain any type.
        my_list_2: list contain any type.
        list_length: length of the list.

    Return:
        a new list (length = list_length) with all divisions.
    """
    div_list = list()
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except TypeError:
            result = 0
            print("wrong type")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            div_list.append(result)
    return div_list
