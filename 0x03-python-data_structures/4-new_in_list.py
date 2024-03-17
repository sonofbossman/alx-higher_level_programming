#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy_my_list = my_list[:]
    if (idx < 0) or (idx > len(my_list) - 1):
        return cpy_my_list
    cpy_my_list[idx] = element
    return cpy_my_list
