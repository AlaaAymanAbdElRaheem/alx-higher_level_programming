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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """return height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting new value to height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
