def factorial(number: int) -> int:
    """Calculate the factorial of a non-negative integer number (non-recursive)."""
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result

# add a fibonacci function
def fibonacci(number: int) -> int:
    """Calculate the n-th Fibonacci number (non-recursive)."""
    if number < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    elif number == 0:
        return 0
    elif number == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, number + 1):
        a, b = b, a + b
    return b


def multiply(a: int, b: int) -> int:
    """Multiply two integers and return the result."""
    return a *