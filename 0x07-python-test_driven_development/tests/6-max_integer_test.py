#!/usr/bin/python3
"""test module for max_intteger function"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """test cases"""

    def test_regular_cases(self):
        """regular"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
        self.assertEqual(max_integer([1, 2, -4, 3]), 3)
        self.assertEqual(max_integer([23]), 23)
        self.assertEqual(max_integer([-1, -2, -4, -3]), -1)
        self.assertEqual(max_integer(['d', 'w', 'b']), 'w')
        self.assertEqual(max_integer('Alaa'), 'l')
        self.assertEqual(max_integer([1.53, 6.33, -9.123, 15.2, 6.0]), 15.2)

    def test_empty_list(self):
        """empty list"""
        self.assertEqual(max_integer([]), None)

    def test_type_error(self):
        """TypeError"""
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer([1, 2, "Alaa"])
        
