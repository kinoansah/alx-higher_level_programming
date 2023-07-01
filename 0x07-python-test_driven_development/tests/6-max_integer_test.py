import unittest
from max_integer import max_integer


class TestMaxInteger(unittest.TestCase):

    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_reversed_list(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([42]), 42)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 0, 10]), 10)

    def test_float_numbers(self):
        self.assertEqual(max_integer([3.14, 2.718, 1.618]), 3.14)


if __name__ == '__main__':
    unittest.main()
