import unittest

"""
This is the function we want to test.
"""
def is_even(number):
    if number % 2 == 0:
        return True
    return False

"""
This is our unit test
"""
class TestEven(unittest.TestCase):

    def test_is_even(self):
        self.assertEqual(is_even(2), True)

    def test_is_uneven(self):
        self.assertEqual(is_even(3), False)


if __name__ == '__main__':
    unittest.main()
