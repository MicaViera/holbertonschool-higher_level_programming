#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for index in matrix:
        length = 1
        for i in index:
            if length == len(index):
                print("{}".format(i), end="")
            else:
                print("{}".format(i), end=" ")
            length += 1
        print()
