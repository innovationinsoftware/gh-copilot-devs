# factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1) 

# create a main function to test the factorial function
def main():
    print(factorial(5))

if __name__ == "__main__":
    main()

    