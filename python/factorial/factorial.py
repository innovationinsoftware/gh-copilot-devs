# Write factorial(n: int) -> int.
# Requirements:
# - Raise ValueError for n < 0
# - 0! and 1! = 1
# - Use an iterative loop (no recursion)
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Negative input is not allowed.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result  