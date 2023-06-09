#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpd_list = my_list.copy()
    if idx < 0:
        return cpd_list
    elif idx > len(my_list):
        return cpd_list
    else:
        cpd_list[idx] = element
        return cpd_list
