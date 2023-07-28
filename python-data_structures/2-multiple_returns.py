#!/usr/bin/python3


# function that returns a tuple with the length of a string and its first character.
def multiple_returns(sentence):
    sentence = []
    length = len(sentence)
    first = sentence[[0]]
    if len(sentence) == 0:
        sentence[0] == None
    else:
        return length, first