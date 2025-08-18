# Build a CLI for factorial:
# - Use argparse to parse -n/--number (default 5)
# - Call factorial() from factorial.py
# - Print "<n>! = <value>" and digits count
# - Exit with error if n is negative
import argparse
from factorial import factorial 

def main():
    parser = argparse.ArgumentParser(description="Calculate factorial of a number.")
    parser.add_argument("-n", "--number", type=int, default=5, help="Number to calculate factorial for")
    args = parser.parse_args()

    try:
        result = factorial(args.number)
        print(f"{args.number}! = {result}")
        print(f"Digits count: {len(str(result))}")
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
