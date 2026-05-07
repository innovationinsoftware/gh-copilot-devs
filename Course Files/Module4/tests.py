import unittest
from testfailure import parse_int_list

class TestParseIntList(unittest.TestCase):

    def test_basic_comma_separated(self):
        self.assertEqual(parse_int_list("1,2,3"), [1, 2, 3])

    def test_single_integer(self):
        self.assertEqual(parse_int_list("42"), [42])

    def test_negative_integers(self):
        self.assertEqual(parse_int_list("-1,-2,-3"), [-1, -2, -3])

    def test_mixed_positive_negative(self):
        self.assertEqual(parse_int_list("-1,0,1,"), [-1, 0, 1])

    def test_large_numbers(self):
        self.assertEqual(parse_int_list("1000000,2000000"), [1000000, 2000000])

    def test_non_numeric_raises_value_error(self):
        with self.assertRaises(ValueError):
            parse_int_list("a,b,c")

    def test_empty_string_raises_value_error(self):
        with self.assertRaises(ValueError):
            parse_int_list("")

    def test_mixed_valid_invalid_raises_value_error(self):
        with self.assertRaises(ValueError):
            parse_int_list("1,two,3")

    def test_returns_list_type(self):
        result = parse_int_list("1,2,3")
        self.assertIsInstance(result, list)

    def test_all_elements_are_int(self):
        result = parse_int_list("1,2,3")
        self.assertTrue(all(isinstance(x, int) for x in result))

if __name__ == "__main__":
    unittest.main()