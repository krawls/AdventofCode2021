import unittest

from day05 import parse_file

class Day05Tests(unittest.TestCase):

    def test_sample(self):
        actual = parse_file('sample.txt',1)
        expected = 5
        self.assertEqual(actual, expected)

    def test_sample2(self):
        actual = parse_file('sample.txt',2)
        expected = 12
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main(verbosity=2)