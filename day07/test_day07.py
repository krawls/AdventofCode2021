import unittest

from day07 import determine_min_fuel_part1
from day07 import determine_min_fuel_part2

class Day07Tests(unittest.TestCase):

    def test_sample(self):
        actual = determine_min_fuel_part1('sample.txt')
        expected = (2, 37)
        self.assertEqual(actual, expected)

    def test_sample2(self):
        actual = determine_min_fuel_part2('sample.txt')
        expected = (5, 168)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main(verbosity=2)