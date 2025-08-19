def compute_average(filename):
    try:
        with open(filename, "r") as f:   
            lines = f.readlines()
            if not lines:
                raise ValueError("The file is empty.")
            total = sum(int(line.strip()) for line in lines)
            avg = total / len(lines)      
            return avg
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
