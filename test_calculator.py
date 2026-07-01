"""Tests for calculator.py."""

import unittest

from calculator import add, subtract


class TestCalculator(unittest.TestCase):
    """A small group of tests for the calculator functions."""

    def test_add_two_numbers(self):
        # This checks that add(2, 3) gives the expected answer: 5.
        self.assertEqual(add(2, 3), 5)

    def test_subtract_two_numbers(self):
        # This checks that subtract(5, 2) gives the expected answer: 3.
        self.assertEqual(subtract(5, 2), 3)


if __name__ == "__main__":
    # This lets beginners run this file directly with: python test_calculator.py
    unittest.main()
