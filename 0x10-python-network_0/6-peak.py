#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """finding a peak with the lowest complexity
    """
    if not list_of_integers:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        return max(list_of_integers)
    elif list_of_integers[0] > list_of_integers[1]:
        return list_of_integers[0]
    elif list_of_integers[-1] > list_of_integers[-2]:
        return list_of_integers[-1]
    else:
        for i in range(1, len(list_of_integers) - 1):
            if list_of_integers[i] >= list_of_integers[i - 1] and\
             list_of_integers[i] >= list_of_integers[i + 1]:
                return list_of_integers[i]
