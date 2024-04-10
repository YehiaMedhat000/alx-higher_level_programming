#!/usr/bin/python3
"""
Script defining a function matrix_divided for sake of learning
to test through using doctest and unittest
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix

    Args:
    matrix -- A list of lists that represents a matrix
    div -- The divisor to be used

    Return:
    A new matrix with the division done
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div != div:
        raise TypeError("div must be a number")

    row_len = len(matrix[0])
    for row in matrix:

        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

        for col in row:
            if isinstance(col, int):
                pass
            elif isinstance(col, float):
                pass
            else:
                raise TypeError(err)
    new_matrix = []
    # Iterate over the rows
    for row in matrix:
        new_row = []

        for col in row:
            try:
                new_row.append(round(col / div, 2))
            except ZeroDivisionError:
                raise ZeroDivisionError("division by zero")

        # Append the new row
        new_matrix.append(new_row)

    return (new_matrix)
