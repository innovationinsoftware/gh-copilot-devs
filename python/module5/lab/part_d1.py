def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * factorial(n - 1)
    # intentionally missing a return

print(factorial(5))
