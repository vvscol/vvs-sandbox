import unittest

import sandbox


class SubtractTest(unittest.TestCase):
    def test_subtracts_two_positive_numbers(self):
        self.assertEqual(sandbox.subtract(5, 3), 2)

    def test_subtracts_negative_numbers(self):
        self.assertEqual(sandbox.subtract(-2, -3), 1)

    def test_subtracts_zero(self):
        self.assertEqual(sandbox.subtract(7, 0), 7)

    def test_subtracts_from_zero(self):
        self.assertEqual(sandbox.subtract(0, 4), -4)

    def test_subtracts_floats(self):
        self.assertAlmostEqual(sandbox.subtract(0.3, 0.1), 0.2)


if __name__ == "__main__":
    unittest.main()
