#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_tobe_delted = []
    for k, v in a_dictionary.items():
        if v == value:
            key_tobe_delted.append(k)
    for ke in key_tobe_delted:
        del a_dictionary[ke]
    return a_dictionary
