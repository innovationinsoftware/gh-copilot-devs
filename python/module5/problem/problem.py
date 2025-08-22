def remove_negatives(numbers):
    for n in numbers:
        if n < 0:
            numbers.remove(n)
    return numbers


data = [3, -1, 5, -2, 7]

#data = [1, -1, -2, 3, -4, -5, 6]

print(remove_negatives(data))