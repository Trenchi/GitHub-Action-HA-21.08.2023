import unittest

from run import add, uppercase


class TestAdd(unittest.TestCase):

    def test_add_function(self):
        self.assertEqual(add(2, 2), 5)
        self.assertEqual(add(4, 4), 17)

    def text_uppercase_make_it_uppercase(self):
        self.assertEqual(uppercase("Baum"), "123")


if __name__ == "__main__":
    unittest.main()