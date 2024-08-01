import unittest
from main import add_int, sub_int

class TestMain(unittest.TestCase):
    def test_add_int(self):
        self.assertEqual(add_int(1,1), 2)
        self.assertEqual(add_int(4,5), 9)

    def test_sub_int(self):
        self.assertEqual(sub_int(10,5), 5)
        self.assertAlmostEqual(sub_int(4,6), -2) # Negative numbers accepted


if __name__ == '__main__':
    unittest.main()