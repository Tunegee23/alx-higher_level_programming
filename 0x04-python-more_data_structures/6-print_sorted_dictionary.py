#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    "print a dict in sorted order of keys"
    if a_dictionary is None:
        return None
    for keys in sorted(a_dictionary.keys()):
        print("{:s}: {}".format(keys, a_dictionary[keys]))
