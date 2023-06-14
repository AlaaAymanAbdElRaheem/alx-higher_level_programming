#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) > 0:
        new_matrix = []
        new_matrix = [[r[i] * r[i] for i in range(len(r))] for r in matrix]
        return new_matrix
