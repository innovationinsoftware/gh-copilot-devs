# This simple banking application models basic transactions such as 
#   deposits, withdrawals, loans, and loan payments. Each function updates and returns the 
#   account balance to demonstrate clear and predictable financial operations.  


# Each function must:
#   Accept a balance parameter
#   Accept an amount parameter
#   Return the updated balance
#   Remain a pure function (no global variables)

# Example function for deposit
def deposit(balance, amount):
    new_balance = balance + amount
    print(f"Deposit of ${amount:,.2f} completed. Updated balance: ${new_balance:,.2f}")
    return new_balance

# Loan function
def loan(balance, amount):
    return balance + amount 

# Withdrawal function   
def withdraw(balance, amount):
    new_balance = balance - amount
    print(f"Withdrawal of ${amount:,.2f} completed. Updated balance: ${new_balance:,.2f}")
    return new_balance

# Loan payment function 
def loan_payment(balance, amount):
    return balance - amount     

