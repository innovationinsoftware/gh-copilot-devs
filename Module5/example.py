def check_value(x):
    message = ""
    magic_number = 10  
    if (y := magic_number):   
        if x > y:
            message = f"x is greater than {y}"
        elif x < y:
            message = f"x is less than {y}"
        else:
            message = f"x is equal to {y}"
    else:
        message = "Condition failed"
    return message
