#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) > 0:
        new_matrix = []
        for row in matrix:
            item =[]
            for i in range(len(row)):
                item.append(row[i] ** 2)
            new_matrix.append(item)
        #new_matrix = [[r[i] ** 2 for i in range(len(r))] for r in matrix]
        return new_matrix
