#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_key = {key: value}
    a_dictionary.update(new_key)
    return a_dictionary
