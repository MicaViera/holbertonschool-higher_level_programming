#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordered_keys = sorted(a_dictionary)
    for key1, key2 in ordered_keys:
        print("{}: {}".format(key1, key2))
