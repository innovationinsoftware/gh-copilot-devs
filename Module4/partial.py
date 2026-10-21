#factorial that list values between 10 and 500
def filter_values(values):
    """Filter a list of integers to include only those between 10 and 500."""
    return [v for v in values if 10 <= v <= 700]  

# Example usage:
data = [5, 15, 250, 600, 45, 800, 1000]
filtered_data = filter_values(data)     
print(filtered_data)

def factorial(n):
    """Calculate the factorial of a non-negative integer n."""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def add(a, b):
    """Return the sum of two values."""
    return a + b

def hello_world():
    """Print a hello world message."""
    print("Hello, world!")