#!/usr/bin/python3
def multiple_returns(sentence):
    f_character = sentence[0]
    length = len(sentence)
    if sentence == "":
        f_character = None
    return length, f_character
