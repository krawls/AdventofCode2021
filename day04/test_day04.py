import unittest

from day04 import win_first
from day04 import win_last

class Day04Tests(unittest.TestCase):

    def test_sample(self):
        actual = win_first('sample.txt')
        expected = (188, 24, 4512)
        self.assertEqual(actual, expected)

    def test_sample2(self):
        actual = win_last('sample.txt')
        expected = (148, 13, 1924)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main(verbosity=2)