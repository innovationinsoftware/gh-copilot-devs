def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

try:
    print(divide_numbers(10, 0))
except ValueError as e:
    print(f"Error: {e}")
