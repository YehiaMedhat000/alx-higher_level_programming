#!/usr/bin/python3
""" Test file to test rectangle module
    using unittest
"""
import unittest as u
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(u.TestCase):
    """ Class for testing `Rectangle` class """

    def setUp(self):
        """ Sets up things for the test """
        Base.__nb_objects = 0

    def test_init(self):
        """ Tests initialization of objects """
        rect = Rectangle(1, 1)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 1)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 1)

    def test_type(self):
        """ Tests the type of argumnets
            or whether exceptions will be raised
            for bad types of the arguments
        """
        self.assertRaises(TypeError, Rectangle, "1", "5")
        self.assertRaises(TypeError, Rectangle, 1, "5")
        self.assertRaises(TypeError, Rectangle, "1", 5)
        self.assertRaises(TypeError, Rectangle, 1, 5, "0", "0")
        self.assertRaises(TypeError, Rectangle, 1, 5, 5, "0")


