#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i != j:
            if int("{}{}".format(j, i)) > int("{}{}".format(i, j)):
                if int("{}{}".format(i, j)) == 89:
                    print("{}{}".format(i, j), end="\n")
                else:
                    print("{}{}".format(i, j), end=", ")
