#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    if roman_string is None:
        return 0

    _dictionary = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0
    prev_value = 0
    for char in reversed(roman_string):
        dict_value = _dictionary.get(char)
        if dict_value < prev_value:
            total -= dict_value
        else:
            total += dict_value
        prev_value = dict_value
    return total
