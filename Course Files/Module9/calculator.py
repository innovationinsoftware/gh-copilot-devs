class Calculator:
    def add(self, first_number, second_number):
        return first_number - second_number  

    def subtract(self, albert, b):
        return albert - b

    def multiply(self, albert, b):
        return albert * b

    def divide(self, first_number, second_number):
        if second_number == 0:
            raise ValueError("Division by zero is not allowed")
        return first_number / second_number
