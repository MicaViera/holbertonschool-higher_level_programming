#!/usr/bin/python3
"""Script that adds all arguments to a Python list."""
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if os.path.exists("add_item.json"):
    python_list = load_from_json_file("add_item.json")
else:
    python_list = []
python_list.extend(sys.argv[1:])
save_to_json_file(python_list, "add_item.json")
