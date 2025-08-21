#create factorial function that is unreadable
def factorial(number):
    """
    Calculate the factorial of a non-negative integer.

    Args:
        number (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of the number.
    """
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)