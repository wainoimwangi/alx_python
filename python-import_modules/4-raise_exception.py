#!/usr/bin/python3


# define raise_exception fucnction
def raise_exception():
    # try convert a string to an integer
    try:
        value = "Error message"
        integer = int(value)
    # catch the type error te using except
    except TypeError as te:
        print("Type error:", te)
        raise te
