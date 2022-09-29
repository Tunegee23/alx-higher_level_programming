#!/usr/bin/python3
def uniq_add(my_list=[]):
    "sum the unique element of my_list"
    if my_list is None:
        return None
    return sum(set(my_list))
