#!/usr/bin/python3
"""
A module that test differents behaviors
of the Base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """
    A class to test the Base Class
    """
    def test_id_is_givin(self):
        """id is given"""
        self.assertTrue(Base(99), self.id == 99)
        self.assertTrue(Base(-99), self.id == -99)
        self.assertTrue(Base(0), self.id == 0)

    def test_id_is_not_givin(self):
        """id is not givin"""
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)

    def test_id_is_None(self):
        """id is None"""
        self.assertTrue(Base(None), self.id == 3)

    def test_to_json_string(self):
        """returns the JSON string representation of list_dictionaries"""
        dic = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_dic = Base.to_json_string(dic)
        self.assertEqual(
            json_dic, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')

    def test_from_json_string(self):
        """returns the list of the JSON string representation json_string"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, [{'height': 4, 'width': 10, 'id': 89},
                                      {'height': 7, 'width': 1, 'id': 7}])
        self.assertEqual(json_list_input,
                         '[{"height": 4, "width": 10, "id": 89},\
 {"height": 7, "width": 1, "id": 7}]')
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89},
                                       {'height': 7, 'width': 1, 'id': 7}])

    def test_create(self):
        """returns an instance with all attributes already set"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 3/5")
