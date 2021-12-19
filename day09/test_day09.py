import unittest

from day09 import risk_level

class Day08Tests(unittest.TestCase):

    def test_sample(self):
        actual = risk_level('sample.txt')
        expected = 15, 1134
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main(verbosity=2)