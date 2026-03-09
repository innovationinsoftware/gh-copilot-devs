def find_duplicates(items):
    duplicates = []

    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j] and items[i] not in duplicates:
                duplicates.append(items[i])

    return duplicates


numbers = [4, 7, 2, 4, 9, 2, 1, 7, 3, 2]
print("Duplicate numbers:", find_duplicates(numbers))

words = ["apple", "banana", "apple", "orange", "banana", "grape"]
print("Duplicate words:", find_duplicates(words))