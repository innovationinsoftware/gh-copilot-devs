import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add_positive_integers(self):
        self.assertEqual(self.calculator.add(2, 3), 5)

    def test_add_negative_and_positive(self):
        self.assertEqual(self.calculator.add(-4, 10), 6)

    def test_subtract_positive_integers(self):
        self.assertEqual(self.calculator.subtract(10, 3), 7)

    def test_subtract_result_negative(self):
        self.assertEqual(self.calculator.subtract(3, 10), -7)

    def test_multiply_positive_integers(self):
        self.assertEqual(self.calculator.multiply(4, 5), 20)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calculator.multiply(9, 0), 0)

    def test_divide_positive_numbers(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calculator.divide(-9, 3), -3)

    def test_divide_by_zero_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "Division by zero is not allowed"):
            self.calculator.divide(10, 0)


if __name__ == "__main__":
    unittest.main()