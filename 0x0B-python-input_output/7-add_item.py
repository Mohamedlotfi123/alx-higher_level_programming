#!/usr/bin/python3
"""
    script that adds all argument to a python list and
    then save them to a file.
"""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

l = list()
for item in load_from_json_file("add_item.json"):
    l.append(item)
for arg in sys.argv[1:]:
    l.append(arg)
save_to_json_file(l, "add_item.json")
