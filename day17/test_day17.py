import unittest

from day17 import max_height

class Day17Tests(unittest.TestCase):

    def test_sample(self):
        actual = max_height('sample.txt')
        expected = (45, 112)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main(verbosity=2)