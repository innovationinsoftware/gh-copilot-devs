def fibonacci_sequence(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[i - 1] + seq[i - 2])
    return seq

print(fibonacci_sequence(15))
