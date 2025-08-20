def add_numbers(first_number, second_number):
    """Add two numbers together."""
    return first_number + second_number

def divide(dividend, divisor):
    """Divide two numbers and handle division by zero."""
    if divisor == 0:
        return "Division by zero is not allowed."
    return dividend / divisor
