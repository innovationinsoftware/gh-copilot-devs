#factorial function
def factorial(number):
    """
    Calculate the factorial of a given number.

    The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
    For example, factorial(5) = 5 * 4 * 3 * 2 * 1 = 120.

    Args:
        number (int): A non-negative integer whose factorial is to be calculated.

    Returns:
        int: The factorial of the given number.
    """
    total = 1
    for i in range(1, number + 1):
        total *= i
    return total

# function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True