#!/usr/bin/python3
"""Write a function that writes a string to a text file."""


def write_file(filename="", text=""):
    """Function that writes a string to a text file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
