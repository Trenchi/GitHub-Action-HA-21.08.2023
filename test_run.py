import unittest

from run import add, uppercase


class TestAdd(unittest.TestCase):

    def test_add_function(self):
        self.assertEqual(add(2, 3), 6)
        self.assertEqual(add(4, 4), 16)

    def text_uppercase_make_it_uppercase(self):
        self.assertEqual(uppercase("Baum"), "BAUM")


if __name__ == "__main__":
    unittest.main()