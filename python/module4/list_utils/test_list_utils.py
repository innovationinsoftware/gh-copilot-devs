import unittest
from list_utils import parse_int_list

class TestParseIntList(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(parse_int_list("1,2,3"), [1, 2, 3])

    def test_spaces(self):
        # Expect whitespace to be ignored
        self.assertEqual(parse_int_list(" 1,  2 ,3 "), [1, 2, 3])

    def test_empty_items(self):
        # Empty tokens should be skipped
        self.assertEqual(parse_int_list("1,,3,"), [1, 3])

    def test_non_numeric(self):
        # Non-numeric tokens should be ignored
        self.assertEqual(parse_int_list("10,a,20,b,30"), [10, 20, 30])

if __name__ == "__main__":
    unittest.main()
# python -m unittest test_list_utils.py