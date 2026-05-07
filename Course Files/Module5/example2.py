def remove_negatives(numbers):
    return [n for n in numbers if n >= 0]

data = [-3, -1, 5, -2, 7]

print(remove_negatives(data))
# Expected output: [3, 5, 7]