#!/usr/bin/python3
"""
    script that adds all argument to a python list and
    then save them to a file.
"""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

my_list = list()
for item in load_from_json_file("add_item.json"):
    my_list.append(item)
for arg in sys.argv[1:]:
    my_list.append(arg)
save_to_json_file(my_list, "add_item.json")
