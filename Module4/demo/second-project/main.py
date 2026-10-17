def total_cost():
    apples = 3.50
    bread = 2.25
    milk = 4.10

    print("Second project")
    print(f"Apples: ${apples:.2f}")
    print(f"Bread: ${bread:.2f}")
    print(f"Milk: ${milk:.2f}")

    total = apples + bread + milk
    print(f"Total: ${total:.2f}")
    return total


if __name__ == "__main__":
    total_cost()
