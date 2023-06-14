#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_num_dic = \
        {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not isinstance(roman_string, str) or roman_string is None:
        return None
    v = []
    result = 0
    for roman in roman_string:
        if roman in roman_num_dic:
            v.append(roman_num_dic[roman])
    for i in v:
        if i <= result:
            result += i
        else:
            result = i - result
    return result
