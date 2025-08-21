import unittest
class TestFactorial(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1, "Factorial of 0 should be 1")

    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1, "Factorial of 1 should be 1")

    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120, "Factorial of 5 should be 120")
        self.assertEqual(factorial(3), 6, "Factorial of 3 should be 6")

    def test_factorial_large_number(self):
        self.assertEqual(factorial(10), 3628800, "Factorial of 10 should be 3628800")

    def test_factorial_negative(self):
        with self.assertRaises(RecursionError, msg="Factorial of negative numbers should raise an error"):
            factorial(-1)