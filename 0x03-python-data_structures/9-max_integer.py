#!/usr/bin/python3

def max_integer(my_list=[]):
    """ find the maximum value od a list"""
    L = len(my_list)
    if L == 0:
        return None

    max = my_list[0]
    for element in my_list:
        if element > max:
            max = element
    return max
