#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for index in matrix:
        length = 1
        for i in index:
            if length == len(index):
                print("{:d}".format(i), end="")
            else:
                print("{:d}".format(i), end=" ")
            length += 1
        print()
