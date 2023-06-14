#!/usr/bin/python3
def uniq_add(my_list=[]):
    set_uniq = set(my_list)
    result = 0
    for num in set_uniq:
        result += num
    return result
