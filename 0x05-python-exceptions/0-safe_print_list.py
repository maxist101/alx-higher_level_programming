#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    val = 0
    for u in range(x):
        try:
            print("{}".format(my_list[u]), end="")
            val += 1
        except IndexError:
            break
    print("")
    return (val)
