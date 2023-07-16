#!/usr/bin/python3
"""
A module that test differents behaviors
of the Rectangle class
"""
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquare(unittest.TestCase):
    """
    A class to test the Square Class
    """
    def test_square_subclass(self):
        """
        Test if Square class inherit from
        Base class and Rectangle class
        """
        self.assertTrue(issubclass(Square, Base))
        self.assertTrue(issubclass(Square, Rectangle))

    def test_attr(self):
        """tests attributes output"""
        s1 = Square(5)
        self.assertTrue(s1.size == 5)
        self.assertTrue(s1.x == 0)
        self.assertTrue(s1.y == 0)
        s2 = Square(2, 2)
        self.assertTrue(s2.size == 2)
        self.assertTrue(s2.x == 2)
        self.assertTrue(s2.y == 0)

    def test_area(self):
        """Test area"""
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(2, 2).area(), 4)
        self.assertEqual(Square(3, 1, 3).area(), 9)

    def test_display(self):
        """test display function"""
        with StringIO() as bufr, redirect_stdout(bufr):
            Square(5).display()
            self.assertEqual(bufr.getvalue(),
                             '#####\n#####\n#####\n#####\n#####\n')
        with StringIO() as bufr, redirect_stdout(bufr):
            Square(3, 1, 3).display()
            self.assertEqual(bufr.getvalue(), '\n\n\n ###\n ###\n ###\n')

    def test_str(self):
        """__str__ method returns [Square] (<id>) <x>/<y> - <size>"""
        s1 = Square(3, 1, 3, 12)
        self.assertEqual(str(s1), "[Square] (12) 1/3 - 3")

    def test_setter_getter(self):
        """test setter and getter methods"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(s1.size, 10)
        with self.assertRaises(TypeError):
            s1.size = "d"
        with self.assertRaises(ValueError):
            s1.size = -5

    def test_update(self):
        """assigns an argument to each attribute:
                  1st argument should be the id attribute
                  2nd argument should be the size attribute
                  3rd argument should be the x attribute
                  4th argument should be the y attribute"""
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(str(s1), '[Square] (10) 0/0 - 5')
        s1.update(1, 2)
        self.assertEqual(str(s1), '[Square] (1) 0/0 - 2')
        s1.update(1, 2, 3)
        self.assertEqual(str(s1), '[Square] (1) 3/0 - 2')
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), '[Square] (1) 3/4 - 2')
        s1.update(x=12)
        self.assertEqual(str(s1), '[Square] (1) 12/4 - 2')
        s1.update(size=7, y=1)
        self.assertEqual(str(s1), '[Square] (1) 12/1 - 7')
        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), '[Square] (89) 12/1 - 7')
        with self.assertRaises(TypeError):
            s1.update(3, 8, 9, (2, 9))
        with self.assertRaises(ValueError):
            s1.update(3, 0, -3, 9)
        with self.assertRaises(TypeError):
            s1.update(size="9", id=89, y=1)
        with self.assertRaises(ValueError):
            s1.update(size=-9, id=89)

    def test_to_dictionary(self):
        """dictionary representation of a Square"""
        s1 = Square(10, 2, 1)
        self.assertEqual(s1.to_dictionary(),
                         {'id': 9, 'x': 2, 'size': 10, 'y': 1})
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(type(s1_dictionary), dict)
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(s1 == s2, False)
