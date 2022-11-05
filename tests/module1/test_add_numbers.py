import unittest

from project.module1.add_numbers import add_numbers


class TestAddNumbers(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(1, 1), 2)


if __name__ == '__main__':
    unittest.main()
