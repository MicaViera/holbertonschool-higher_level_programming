#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for elements in range(x):
            print(my_list[elements], end="")
    except:
        print()
        return elements
    print()
    return x