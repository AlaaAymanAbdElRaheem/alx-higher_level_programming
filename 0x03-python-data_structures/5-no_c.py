#!/usr/bin/env python3
def no_c(my_string):
    if len(my_string) > 0:
        str_list = []
        for let in my_string:
            if let != 'c' and let != 'C':
                str_list.append(let)
        my_string = ''
        for let in str_list:
            my_string += let
        return my_string
