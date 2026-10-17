#factorial that list values between 10 and 500
def filter_values(values):
    """Filter a list of integers to include only those between 10 and 500."""
    return [v for v in values if 10 <= v <= 700]  

# Example usage:
data = [5, 15, 250, 600, 45, 800, 1000]
filtered_data = filter_values(data)     
print(filtered_data)