#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2 and len(tuple_b) < 2:
        if len(tuple_a) == 0 and len(tuple_b) == 0:
            x = 0
            y = 0
        elif len(tuple_a) == 0 and len(tuple_b) != 0:
            x = tuple_b[0]
            y = 0
        elif len(tuple_a) != 0 and len(tuple_b) == 0:
            x = tuple_a[0]
            y = 0
        else:
            x = tuple_a[0] + tuple_b[0]
            y = 0
    elif len(tuple_a) < 2 and len(tuple_b) >= 2:
        if len(tuple_a) != 0:
            x = tuple_a[0] + tuple_b[0]
            y = tuple_b[1]
        else:
            x = tuple_b[0]
            y = tuple_b[1]
    elif len(tuple_b) < 2 and len(tuple_a) >= 2:
        if len(tuple_b) != 0:
            x = tuple_a[0] + tuple_b[0]
            y = tuple_a[1]
        else:
            x = tuple_a[0]
            y = tuple_a[1]
    else:
        x = tuple_a[0] + tuple_b[0]
        y = tuple_a[1] + tuple_b[1]
    return (x, y)
