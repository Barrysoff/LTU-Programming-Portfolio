from io import StringIO
from unittest.mock import patch


from lecture_04_01 import Hypercube

import unittest

class TestHypercube(unittest.TestCase):

    def test_initialization(self):
        h = Hypercube(2, 10)
        self.assertEqual(h.getDimension(), 2)
        self.assertEqual(h.getLength(), 10)

    def test_getDimension(self):
        h = Hypercube(2, 10)
        self.assertEqual(h.getDimension(), 2)

    def test_getLength(self):
        h = Hypercube(3, 6)
        self.assertEqual(h.getLength(), 6)

    def test_setLength_positive(self):
        h = Hypercube(3, 8)
        h.setLength(5)
        self.assertEqual(h.getLength(), 5)

    def test_setLength_negative(self):
        h = Hypercube(4, 9)
        with self.assertRaises(ValueError) as err:
            h.setLength(-3)

        self.assertEqual(str(err.exception), "Length must be non-negative")

        self.assertEqual(h.getLength(), 9)

    def test_whatAmI(self):
        h = Hypercube(2, 10)
        with patch('sys.stdout', new=StringIO()) as newout:
            h.whatAmI()
            output = newout.getvalue().strip()
        self.assertEqual(output, "I am a 2 dimensional hypercube")

if __name__ == '__main__':
    unittest.main()