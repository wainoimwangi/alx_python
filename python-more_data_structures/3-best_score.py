#!/usr/bin/python3

# function that returns a key with the biggest integer value
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    Score = 0
    Score_key = ""
    for key, value in a_dictionary.items():
        if value > Score:
            Score = value
            Score_key = key
    return Score_key