def remove_negatives(numbers):
    def remove_negatives(numbers):
        return [n for n in numbers if n >= 0]

    data = [3, -1, 5, -2, 7]
    print(remove_negatives(data))
        if n < 0:
            numbers.remove(n)
    return numbers

data = [3, -1, 5, -2, 7]

#data = [1, -1, -2, 3, -4, -5, 6]

print(remove_negatives(data))