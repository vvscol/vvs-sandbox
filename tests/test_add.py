import unittest

import sandbox


class AddTest(unittest.TestCase):
    def test_adds_two_positive_numbers(self):
        self.assertEqual(sandbox.add(2, 3), 5)

    def test_adds_negative_numbers(self):
        self.assertEqual(sandbox.add(-2, -3), -5)

    def test_adds_zero(self):
        self.assertEqual(sandbox.add(7, 0), 7)

    def test_adds_floats(self):
        self.assertAlmostEqual(sandbox.add(0.1, 0.2), 0.3)


if __name__ == "__main__":
    unittest.main()
