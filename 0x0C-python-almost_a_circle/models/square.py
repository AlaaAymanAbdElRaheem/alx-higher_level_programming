#!/usr/bin/python3
"""
Module contains class Square

Inherits from Rectangle;
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """implementation"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialization"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """getter"""
        return self.width

    @size.setter
    def size(self, value):
        """setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """return [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute:
                  1st argument should be the id attribute
                  2nd argument should be the size attribute
                  3rd argument should be the x attribute
                  4th argument should be the y attribute"""
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for i in range(len(args)):
                if i > 3:
                    break
                else:
                    setattr(self, attrs[i], args[i])
        else:
            for k, v in kwargs.items():
                if k in attrs:
                    setattr(self, k, v)
