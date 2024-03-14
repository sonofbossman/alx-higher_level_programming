#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_len = len(sys.argv) - 1
    arg_lst = sys.argv
    res = 0
    if arg_len >= 1:
        for i in range(arg_len):
            res += int(arg_lst[i+1])
    print("{}".format(res))
