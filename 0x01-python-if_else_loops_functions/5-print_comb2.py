#!/usr/bin/python3
for num in range(100):
    if num == 99:
        print(num)
    else:
        print('{0:02d}'.format(num), end=", ")
