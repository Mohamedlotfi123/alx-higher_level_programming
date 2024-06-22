#!/usr/bin/python3
""" Unittest for max_integer function. """
import unittest


class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        self.assertEqual(max_integer([4]), 4)

    def test_multi_element_list(self):
        self.assertEqual(max_integer([3, 4, 5, 6, 7]), 7)
        self.assertEqual(max_integer([-1, -3, -69, -34]), -1)
        self.assertEqual(max_integer([0, -556, 4]), 4)
        self.assertEqual(max_integer([1.5, 5.35, -3.2, 5]), 5.35)
