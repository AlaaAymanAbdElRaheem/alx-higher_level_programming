#!/usr/bin/python3
"""defining class Rectangle that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """implement  Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """inizialing the class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """implement area function"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for x in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + '#' * self.__width)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute:
                  1st argument should be the id attribute
                  2nd argument should be the width attribute
                  3rd argument should be the height attribute
                  4th argument should be the x attribute
                  5th argument should be the y attribute"""

        attrs = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i in range(len(args)):
                if i > 4:
                    break
                else:
                    setattr(self, attrs[i], args[i])
        else:
            for k, v in kwargs.items():
                if k in attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle:
            This dictionary contains:
                                     id
                                     width
                                     height
                                       x
                                       y"""
        dic = {}
        dic["id"] = self.id
        dic["width"] = self.width
        dic["height"] = self.height
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
