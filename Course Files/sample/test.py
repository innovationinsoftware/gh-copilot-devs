def add(a: int, b: int) -> int:
	return a + b


def subtract(a: int, b: int) -> int:
	return a - b


def factorial(n: int) -> int:
	if n < 0:
		raise ValueError("n must be a non-negative integer")

	result = 1
	for value in range(2, n + 1):
		result *= value

	return result


    
