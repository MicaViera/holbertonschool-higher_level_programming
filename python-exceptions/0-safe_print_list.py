#!/usr/bin/python3 
def safe_print_list(my_list=[], x=0): 
    elements_print = 0 
    try: 
        for elements in range(x): 
            print(my_list[elements], end="") 
            elements_print += 1 
    except Exception: 
        print() 
        return elements
    print() 
    return x
