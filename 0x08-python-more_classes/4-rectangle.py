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

    def area(self):
        """ returns the area"""
        return self.__width * self.__height

    def perimeter(self):
        """ returns perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__width + self.__height)

    def __str__(self):
        """prints #"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rec_str = ""
        for i in range(self.__height):
            rec_str += ("#" * self.__width) + '\n'
        return rec_str.strip("\n")

    def __repr__(self):
        """string representation"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
