#!/usr/bin/python3


# function that returns a tuple with the length of a string and its first character.
def multiple_returns(sentence):
    if not sentence:
        return 0, None
    else:
        length = len(sentence)
        first = sentence[0]
        return length, first