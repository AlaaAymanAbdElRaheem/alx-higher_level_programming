#!/usr/bin/python3
"""adding attributes"""


class Rectangle:
    """difine a rectangle"""
    def __init__(self, width=0, height=0):
        """intialaize attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """return width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting width value"""
        if type(value) is int and value > 0:
            self.__width = value
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """return height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting new value to height"""
        if type(value) is int and value > 0:
            self.__height = value
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
