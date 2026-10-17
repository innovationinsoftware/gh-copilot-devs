import unittest
from parse_int_list import parse_int_list

class TestParseIntList(unittest.TestCase):
    def test_basic_parse(self):
        s = "1,2,3"
        result = parse_int_list(s)
        self.assertEqual(result, [1, 2, 3])
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(x, int) for x in result))

    def test_whitespace_handling(self):
        s = " 1, 2 ,3 "
        result = parse_int_list(s)
        self.assertEqual(result, [1, 2, 3])

    def test_negative_and_zero(self):
        s = "-1,0,2"
        result = parse_int_list(s)
        self.assertEqual(result, [-1, 0, 2])

    def test_plus_sign_numbers(self):
        s = "+1,-2"
        result = parse_int_list(s)
        self.assertEqual(result, [1, -2])

    def test_single_large_number(self):
        s = "12345678901234567890"
        result = parse_int_list(s)
        self.assertEqual(result, [12345678901234567890])

    def test_empty_string_raises(self):
        with self.assertRaises(ValueError):
            parse_int_list("")

    def test_consecutive_commas_raises(self):
        with self.assertRaises(ValueError):
            parse_int_list("1,,3")

    def test_trailing_comma_raises(self):
        with self.assertRaises(ValueError):
            parse_int_list("1,2,")

    def test_non_numeric_token_raises(self):
        with self.assertRaises(ValueError):
            parse_int_list("a,2")

    def test_only_whitespace_raises(self):
        with self.assertRaises(ValueError):
            parse_int_list("   ")

    def test_internal_whitespace_only_token_raises(self):
        with self.assertRaises(ValueError):
            parse_int_list("1, ,3")

    def test_newline_whitespace(self):
        s = "1,\n2, 3"
        result = parse_int_list(s)
        self.assertEqual(result, [1, 2, 3])

if __name__ == "__main__":
    unittest.main()
