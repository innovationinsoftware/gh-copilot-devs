def compute_average(filename):
    with open(filename, "r") as f:
        numbers = [int(line.strip()) for line in f.readlines()]
        return sum(numbers) / len(numbers)

print(compute_average("grades.txt"))
