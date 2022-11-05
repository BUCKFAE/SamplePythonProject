import unittest

from project.module2.subract_numbers import subtract_numbers


class TestSubtractNumbers(unittest.TestCase):

    def test_subtract_numbers(self):
        self.assertEqual(subtract_numbers(2, 3), -1)

if __name__ == '__main__':
    unittest.main()