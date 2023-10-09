#!/usr/bin/python3
"""Write a function that appends a string at the end of a text file."""


def append_write(filename="", text=""):
    """Function that appends the string."""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
