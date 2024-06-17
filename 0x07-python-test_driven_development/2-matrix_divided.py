#!/usr/bin/python3
""" matrix_divided function """


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.

    Args:
        matrix: list of lists of integers or floats.
        div: integer or float for the division.

    Raises:
        TypeError: if matrix is not list of lists of
                    integer or float.
        TypeError: if the rows of a matrix is not of
                    the same size.
        ZeroDivisionError: if div is zero.

    Return:
        the new matrix after division.
    """
    n_matrix = list()

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for List in matrix:
        row = list()
        if type(List) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(List) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in List:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            ele = round(element / div, 2)
            row.append(ele)
        n_matrix.append(row)
    return n_matrix
