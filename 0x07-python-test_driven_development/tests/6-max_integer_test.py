#!/usr/bin/python3
"""test module for max_intteger function"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """test cases"""

    def regular_cases(self):
        """regular"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
        self.assertEqual(max_integer([1, 2, -4, 3]), 3)
        self.assertEqual(max_integer([23]), 23)
        self.assertEqual(max_integer([-1, -2, -4, -3]), -1)

    def empty_list(self):
        """empty list"""
        self.assertEqual(max_integer([]), None)
        
