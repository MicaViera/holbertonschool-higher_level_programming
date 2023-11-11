#!/usr/bin/python3
"""Function that returns the dictionary description."""


def class_to_json(obj):
    """Function that serializes a class."""
    return obj.__dict__
