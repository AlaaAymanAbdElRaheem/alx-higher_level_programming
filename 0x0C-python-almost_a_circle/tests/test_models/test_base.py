#!/usr/bin/python3
"""
A module that test differents behaviors
of the Base class
"""
import unittest
from models.base import Base


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
