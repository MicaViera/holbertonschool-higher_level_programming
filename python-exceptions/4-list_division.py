#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    final_list = []
    try:
        for elements in range(list_length):
            final_list.append(my_list_1[elements] / my_list_2[elements])
    except IndexError:
        final_list.append(0)
        print("out of range")
    except TypeError:
        final_list.append(0)
        print("wrong type")
    except ZeroDivisionError:
        final_list.append(0)
        print("division by 0")
    finally:
        return final_list
