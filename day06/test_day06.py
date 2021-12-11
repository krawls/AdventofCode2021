import unittest

from day06 import count_lanternfish

class Day06Tests(unittest.TestCase):

    def test_sample(self):
        actual = count_lanternfish('sample.txt',80)
        expected = 5934
        self.assertEqual(actual, expected)

    def test_sample2(self):
        actual = count_lanternfish('sample.txt',256)
        expected = 26984457539
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main(verbosity=2)