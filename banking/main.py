from accounts import BankError
from bank import Bank
from factories import FACTORIES

MENU = """
1) Open account   2) Deposit   3) Withdraw   4) Transfer
5) Balance        6) Statement 7) Apply interest 8) List accounts
0) Exit
"""


def main():
    bank = Bank()
    while True:
        print(MENU)
        choice = input("> ").strip()
        try:
            if choice == "1":
                kind = input(f"Type {list(FACTORIES)}: ")
                a = bank.open_account(input("Owner: "), kind)
                print(f"Opened {a.type_name} account {a.number}")
            elif choice == "2":
                bank.deposit(input("Account: "), input("Amount: "))
            elif choice == "3":
                bank.withdraw(input("Account: "), input("Amount: "))
            elif choice == "4":
                bank.transfer(input("From: "), input("To: "), input("Amount: "))
            elif choice == "5":
                print(bank.get(input("Account: ")).balance)
            elif choice == "6":
                print(bank.statement(input("Account: ")))
            elif choice == "7":
                for num, amt in bank.apply_interest().items():
                    print(f"{num}: +{amt}")
            elif choice == "8":
                for a in bank.accounts():
                    print(f"{a.number} {a.type_name:<9} {a.owner:<15} {a.balance}")
            elif choice == "0":
                break
            else:
                print("Invalid choice")
        except BankError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
