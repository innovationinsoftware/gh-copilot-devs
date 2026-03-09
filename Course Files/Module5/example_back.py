
def remove_negatives(numbers):
    for n in numbers:
        if n < 0:
            numbers.remove(n)
    return numbers

data = [3, -1, 5, -2, 7]
print(remove_negatives(data))
# Expected output: [3, 5, 7]@