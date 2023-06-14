#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    result = 0
    div = 0
    for tub in my_list:
        result += tub[0] * tub[1]
        div += tub[1]
    return result / div
