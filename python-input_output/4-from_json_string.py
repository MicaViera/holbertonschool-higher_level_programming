#!/usr/bin/python3
"""Function that  returns an object represented by a JSON string."""
import json


def from_json_string(my_str):
    """Function that an object from a json representation."""
    object_rep = json.loads(my_str)
    return object_rep
