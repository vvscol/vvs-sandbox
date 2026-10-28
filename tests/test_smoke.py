import unittest

import sandbox


class SmokeTest(unittest.TestCase):
    def test_package_imports(self):
        self.assertTrue(sandbox.__doc__)


if __name__ == "__main__":
    unittest.main()
