#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) > 0:
        new_matrix = []
        for row in matrix:
            new_matrix.append(list(map(lambda x: x ** 2, row)))
        return new_matrix
