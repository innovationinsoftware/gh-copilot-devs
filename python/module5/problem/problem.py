def remove_negatives(numbers):
    return [n for n in numbers if n >= 0]

data = [1, -1, -2, 3, -4, -5, 6]

print(remove_negatives(data))