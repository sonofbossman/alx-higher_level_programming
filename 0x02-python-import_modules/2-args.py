#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_len = len(sys.argv) - 1
    arg_lst = sys.argv
    if arg_len >= 1:
        if arg_len != 1:
            print("{} arguments:".format(arg_len))
        else:
            print("{} argument:".format(arg_len))
        for i in range(arg_len):
            print("{}: {}".format(i+1, arg_lst[i+1]))
    else:
        print("{} arguments.".format(arg_len))
