#!/usr/bin/python3


# function that returns a tuple with the length of a string and its first character.
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    if length == 0:
        return 0, None
    else:
        return length, first