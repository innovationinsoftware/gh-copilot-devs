import unittest
from division import divide


class TestDivide(unittest.TestCase):
    def test_exact_division(self):
        self.assertEqual(divide(10, 2), 5)

    def test_returns_float(self):
        self.assertIsInstance(divide(10, 2), float)

    def test_non_integer_result(self):
        self.assertAlmostEqual(divide(1, 3), 0.3333333333, places=9)

    def test_negative_numbers(self):
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(10, -2), -5)
        self.assertEqual(divide(-10, -2), 5)

    def test_zero_numerator(self):
        self.assertEqual(divide(0, 5), 0)

    def test_float_inputs(self):
        self.assertAlmostEqual(divide(7.5, 2.5), 3.0)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)


if __name__ == "__main__":
    unittest.main()
