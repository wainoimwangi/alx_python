#!/usr/bin/python3


# define raise_exception fucnction
def raise_exception():
    # try convert a string to an integer
    try:
        value = "I love python"
        convert = int(value)
    # catch the type error te using except
    except TypeError as e:
        print("Exception raised", e)
        raise e
