def factorial(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
    return b

#create a main function to test the above functions

#def main():
print("Factorial of 5:", factorial(5))  # Output: 120
print("Fibonacci of 10:", fibonacci(10))  # Output: 55  