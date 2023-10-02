#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_elements_printed = 0
    try:
        for element in range(x):
            print("{:d}".format(my_list[element]), end="")
            num_elements_printed += 1
    except (TypeError, ValueError):
        pass
    print()
    return num_elements_printed
