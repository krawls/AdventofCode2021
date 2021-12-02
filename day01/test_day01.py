import unittest

from day01 import count_depth_measurements
from day01 import count_depth_measurements_three_window

class Day01Tests(unittest.TestCase):

    def test_sample(self):
        actual = count_depth_measurements('sample.txt')
        expected = 7
        self.assertEqual(actual, expected)

    def test_sample(self):
        actual = count_depth_measurements_three_window('sample.txt')
        expected = 5
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main(verbosity=2)