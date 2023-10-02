#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result_division = a / b
    except Exception:
        result_division = None
    finally:
        print("Inside result: {}".format(result_division))
        return result_division
