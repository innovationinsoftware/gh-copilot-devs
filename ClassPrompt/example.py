def factorial(n):
	if n < 0:
		raise ValueError("factorial is not defined for negative numbers")

	result = 1
	for value in range(2, n + 1):
		result *= value
	return result
