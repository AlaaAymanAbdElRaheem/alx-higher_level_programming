#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or not bool(a_dictionary):
        return None
    else:
        result = 0
        best_key = ''
        for k, v in a_dictionary.items():
            if v > result:
                result = v
                best_key = k
    return best_key
