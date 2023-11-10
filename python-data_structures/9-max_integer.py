#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    new_list = sorted(my_list)
    return (new_list[(len(my_list) - 1)])
