# create a factorial function that is non recursive
def factorial(n: int) -> int:
    """Calculate the factorial of a number iteratively."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result