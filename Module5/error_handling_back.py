def compute_average(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        total = sum(int(line.strip()) for line in lines)
        avg = total / len(lines) 
return avg
