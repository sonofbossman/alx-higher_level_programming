#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    char_pos = 0
    for char in str:
        if char_pos != n:
            new_str += char
        char_pos += 1
    return new_str
