from utils import add_numbers, divide_numbers

def main():
    print("GitHub Copilot @workspace and @terminal Lab")
    print("--------------------------------------------")

    a = 10
    b = 5

    total = add_numbers(a, b)
    print(f"The sum of {a} and {b} is {total}")

    result = divide_numbers(a, b)
    print(f"{a} divided by {b} is {result}")

if __name__ == "__main__":
    main()