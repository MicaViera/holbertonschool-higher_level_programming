#!/usr/bin/python3
def uniq_add(my_list=[]):
    list = set(my_list)
    uniq_list = 0
    if my_list:
        for int in list:
            uniq_list += int
    return uniq_list
