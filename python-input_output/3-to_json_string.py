#!/usr/bin/python3
"""Function that returns the json representation of an object."""
import json


def to_json_string(my_obj):
    """Method that returns a json representation."""
    json_rep = json.dumps(my_obj)
    return json_rep
