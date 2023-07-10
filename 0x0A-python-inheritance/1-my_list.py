#!/usr/bin/python3
"""defining a class MyList that inherits from list"""


class MyList(list):
    """ MyList class"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        self.sort()
        print(self)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
