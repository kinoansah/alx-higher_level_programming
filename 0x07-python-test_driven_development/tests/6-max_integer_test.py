#!/usr/bin/python3
"""Unittest for max_integer([...])
"""

import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # Test case 1: List with positive integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        # Test case 2: List with positive and negative integers
        self.assertEqual(max_integer([1, 3, -4, 2]), 3)

        # Test case 3: List with negative integers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

        # Test case 4: Empty list
        self.assertEqual(max_integer([]))

        # Test case 5: List with one element
        self.assertEqual(max_integer([5]), 5)

        # Test case 6: List with duplicate maximum value
        self.assertEqual(max_integer([3, 5, 9, 5]), 9)

        # Test case 7: List with duplicate minimum value
        self.assertEqual(max_integer([-3, -5, -9, -5]), -3)

if __name__== '__main__':
    unittest.main()
