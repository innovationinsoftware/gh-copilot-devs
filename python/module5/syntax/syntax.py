def check_value(x):
    message = ""
    magic_number = 10

    if x > magic_number:
        message = f"x is greater than {magic_number}"
    elif x < magic_number:
        message = f"x is less than {magic_number}"
    else:
        message = f"x is equal to {magic_number}"

    return message


print(check_value(5))   # Output: "x is less than 10"
print(check_value(10))  # Output: "x is equal to 10"
print(check_value(20))  # Output: "x is greater than 10"