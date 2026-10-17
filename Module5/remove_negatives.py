def remove_negatives(numbers):
    for n in numbers:
        if n < 0:
            numbers.remove(n)
    return numbers

data = [3, -1, -2, 5, 7]
print(remove_negatives(data))
