#!/usr/bin/python3
"""defining matrix_divided function"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix"""
    if div is None:
        raise TypeError("matrix_divided()\
 missing 1 required positional argument: 'div'")
    elif matrix is None and div is None:
        raise TypeError("matrix_divided()\
 missing 2 required positional arguments: 'matrix' and 'div'")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")

    row_len = 0
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")
        if len(row) != row_len and row_len != 0:
            raise TypeError("Each row of the matrix must have the same size")
        row_len = len(row)
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")

    new_mat = [[round(x / div, 2) for x in row] for row in matrix]
    return new_mat


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
