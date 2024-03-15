#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, mul, div, sub
    import sys
    arg_len = len(sys.argv) - 1
    arg_lst = sys.argv
    accepted_op = ["+", "-", "*", "/"]
    if arg_len != 3:
        print("Usage: {} <a> <operator> <b>".format(arg_lst[0]))
        sys.exit(1)
    else:
        a = int(arg_lst[1])
        op = arg_lst[2]
        b = int(arg_lst[3])
        if op in accepted_op:
            if op == "+":
                print("{} {} {} = {}".format(a, op, b, add(a, b)))
            elif op == "-":
                print("{} {} {} = {}".format(a, op, b, sub(a, b)))
            elif op == "*":
                print("{} {} {} = {}".format(a, op, b, mul(a, b)))
            elif op == "/":
                print("{} {} {} = {}".format(a, op, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
