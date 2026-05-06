def process_transaction(balance, amount, transaction_type, overdraft_limit=0):
    """
    Processes a banking transaction and returns the updated balance.
    """

    if amount <= 0:
        raise ValueError("Transaction amount must be positive.")

    if transaction_type == "deposit":
        balance += amount

    elif transaction_type == "withdrawal":
        if balance - amount < -overdraft_limit:
            raise ValueError("Overdraft limit exceeded.")
        balance -= amount

    elif transaction_type == "loan":
        balance += amount

    elif transaction_type == "loan_payment":
        if amount > balance:
            raise ValueError("Loan payment cannot exceed current balance.")
        balance -= amount

    else:
        raise ValueError("Invalid transaction type.")

    return balance

#add a main routine to test the function
if __name__ == "__main__":
    balance = 1000
    print("Initial balance:", balance)

    try:
        balance = process_transaction(balance, 200, "deposit")
        print("After deposit:", balance)

        balance = process_transaction(balance, 500, "withdrawal")
        print("After withdrawal:", balance)

        balance = process_transaction(balance, 300, "loan")
        print("After loan:", balance)

        balance = process_transaction(balance, 100, "loan_payment")
        print("After loan payment:", balance)

    except ValueError as e:
        print("Error:", e)