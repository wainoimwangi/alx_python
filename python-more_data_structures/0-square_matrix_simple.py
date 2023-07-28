#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    for row in matrix:
        for i, element in enumerate(row):
            print("{:d}".format(element), end=" " if i < len(row) - 1 else '')
    square = []
    for row in matrix:
        square_row = []
        for i, element in enumerate(row):
            square_row.append(element ** 2)
        square.append(square_row)
    return square
