#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for li in matrix:
        i = 0
        for j in li:
            i += 1
            if i < len(li):
                print("{} ".format(j), end='')
            else:
                print("{}".format(j), end='')
        print()
