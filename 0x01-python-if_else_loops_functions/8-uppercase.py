#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for char in str:
        if 'a' <= char <= 'z':
            upper_char = chr(ord(char) - 32)
        else:
            upper_char = char
        upper_str += upper_char
    print(upper_str)
