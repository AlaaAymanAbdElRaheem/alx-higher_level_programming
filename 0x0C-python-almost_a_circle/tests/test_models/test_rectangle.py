#!/usr/bin/python3
"""
A module that test differents behaviors
of the Rectangle class
"""
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """
    A class to test the Rectangle Class
    """
    def test_rectangle_subclass(self):
        """
        Test if Rectangle class inherit from
        Base class
        """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_attr(self):
        """tests attributes output"""
        r1 = Rectangle(10, 2)
        self.assertTrue(r1.width == 10)
        self.assertTrue(r1.height == 2)
        self.assertTrue(r1.x == 0)
        self.assertTrue(r1.y == 0)

    def test_type_error(self):
        """test if the values not integer"""
        with self.assertRaises(TypeError):
             Rectangle(None)
        with self.assertRaises(TypeError):
             Rectangle("3",7)
        with self.assertRaises(TypeError):
             Rectangle(3 ,"9")
        with self.assertRaises(TypeError):
             Rectangle(3 ,8, [87,7],2)
        with self.assertRaises(TypeError):
             Rectangle(3 ,8, 9,(2,9))
        with self.assertRaises(TypeError):
             Rectangle({3: 9} ,8, 9)
        with self.assertRaises(TypeError):
            Rectangle(True, 4)
        with self.assertRaises(TypeError):
            Rectangle(5, 1, 1, 1.53)

    def test_value_error(self):
        """tests if the value is not valid"""
        with self.assertRaises(ValueError):
             Rectangle(-3,7)
        with self.assertRaises(ValueError):
             Rectangle(3,-7)
        with self.assertRaises(ValueError):
             Rectangle(3, 7, -3, 9)
        with self.assertRaises(ValueError):
             Rectangle(3, 7, 3, -9)
        with self.assertRaises(ValueError):
             Rectangle(3, 7, -3, 9)
        with self.assertRaises(ValueError):
             Rectangle(0, 7, 3, 9)
        with self.assertRaises(ValueError):
             Rectangle(3, 0, -3, 9)

    def test_area(self):
        """Test area"""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10, 0, 0).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)


    def test_display(self):
        """test display function"""
        with StringIO() as bufr, redirect_stdout(bufr):
            Rectangle(4, 6).display()
            self.assertEqual(bufr.getvalue(), '####\n####\n####\n####\n####\n####\n')
        with StringIO() as bufr, redirect_stdout(bufr):
            Rectangle(2, 3, 2, 2).display()
            self.assertEqual(bufr.getvalue(), '\n\n  ##\n  ##\n  ##\n')


    def test_str(self):
        """__str__ method returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        """assigns an argument to each attribute:
                  1st argument should be the id attribute
                  2nd argument should be the width attribute
                  3rd argument should be the height attribute
                  4th argument should be the x attribute
                  5th argument should be the y attribute"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 10/10')
        r1.update(89, 2)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 2/10')
        r1.update(89, 1, 2)
        self.assertEqual(str(r1), '[Rectangle] (89) 10/10 - 1/2')
        r1.update(99, 1, 2, 3, 4)
        self.assertEqual(str(r1), '[Rectangle] (99) 3/4 - 1/2')
        with self.assertRaises(TypeError):
             r1.update(3 ,8, 9,(2,9))
        with self.assertRaises(ValueError):
             r1.update(3, 0, -3, 9)
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(str(r1), '[Rectangle] (9) 10/10 - 10/1')
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), '[Rectangle] (9) 2/10 - 1/1')
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), '[Rectangle] (89) 3/1 - 2/1')
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), '[Rectangle] (89) 1/3 - 4/2')

    def test_to_dictionary(self):
        """dictionary representation of a Rectangle"""
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(r1.to_dictionary(), {'x': 1, 'y': 9, 'id': 6, 'height': 2, 'width': 10})
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(type(r1_dictionary), dict)
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(r1 == r2, False)
        
