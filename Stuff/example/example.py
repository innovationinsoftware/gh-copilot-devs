def add(a, b):
    return a + b


def subtract(minuend, subtrahend):
    return minuend - subtrahend


def divide(dividend, divisor):
    if divisor == 0:
        raise ValueError("Cannot divide by zero")
    return dividend / divisor

