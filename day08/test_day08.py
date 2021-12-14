import unittest

from day08 import decode_segments

class Day08Tests(unittest.TestCase):

    def test_sample(self):
        actual = decode_segments('sample.txt', 1)
        expected = 26
        self.assertEqual(actual, expected)

    def test_sample2(self):
        actual = decode_segments('sample.txt', 2)
        expected = 61229
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main(verbosity=2)