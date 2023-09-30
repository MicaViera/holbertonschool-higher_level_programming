#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nmatrix = []
    if matrix:
        for number in matrix:
            nmatrix.append(list(map(lambda value: value ** 2, number)))
        return nmatrix
