#!/usr/bin/python3
"""Function that removes all characters c and C from a string."""


def no_c(my_string):
    """"""
    new_string = ""

    for a in my_string:
        if a != 'c' and a != 'C':
            new_string += 1
    return new_string
