#!/usr/bin/python3
"""defining MyInt Class"""


class MyInt(int):
    def __init__(self, num):
        self.num = num

    def __eq__(self, num2):
        return self.num != num2

    def __ne__(self, num2):
        return self.num == num2
