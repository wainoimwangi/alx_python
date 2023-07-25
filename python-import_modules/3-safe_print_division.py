#!/usr/bin/python3
# function definition
def safe_print_division(a, b):
    a, b
    try: 
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result