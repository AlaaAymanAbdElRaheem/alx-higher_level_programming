#!/usr/bin/python3
def max_integer(my_list=[]):
    max_int = min(my_list)
    if len(my_list) == 0:
        return None
    else:
        for i in my_list:
            if i > max_int:
                max_int = i
        return max_int
