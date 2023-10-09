#!/usr/bin/python3
"""Function that returns True if the object is an instance of, or if the
object is an instance of a class that inherited from."""


def is_kind_of_class(obj, a_class):
    """Function that returns True or False."""
    if isinstance(obj, a_class):
        return True
    else:
        return False
