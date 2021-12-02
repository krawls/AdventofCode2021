import unittest

from day02 import determine_position
from day02 import determine_position2

class Day01Tests(unittest.TestCase):

    def test_sample(self):
        actual = determine_position('sample.txt')
        expected = (15, 10, 150)
        self.assertEqual(actual, expected)

    def test_sample2(self):
        actual = determine_position2('sample.txt')
        expected = (15, 60, 900)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main(verbosity=2)