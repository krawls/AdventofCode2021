import unittest

from day03 import determine_power_consumption
from day03 import determine_life_support_rating

class Day03Tests(unittest.TestCase):

    def test_sample(self):
        actual = determine_power_consumption('sample.txt')
        expected = (22, 9, 198)
        self.assertEqual(actual, expected)

    def test_sample2(self):
        actual = determine_life_support_rating('sample.txt')
        expected = (23, 10, 230)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main(verbosity=2)