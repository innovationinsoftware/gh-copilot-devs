from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from policies import FeePolicy, InterestPolicy, money


class BankError(Exception):
    pass


class InsufficientFunds(BankError):
    pass


@dataclass
class Transaction:
    kind: str
    amount: Decimal
    balance_after: Decimal
    timestamp: datetime


class Account:
    type_name = "Account"

    def __init__(self, number: str, owner: str, fee_policy: FeePolicy,
                 interest_policy: InterestPolicy, overdraft_limit="0"):
        self.number = number
        self.owner = owner
        self.fee_policy = fee_policy
        self.interest_policy = interest_policy
        self.overdraft_limit = money(overdraft_limit)
        self.balance = Decimal("0.00")
        self.history: list[Transaction] = []

    @staticmethod
    def _validate(amount) -> Decimal:
        try:
            amount = money(amount)
        except ArithmeticError:
            raise BankError("Invalid amount") from None
        if amount <= 0:
            raise BankError("Amount must be positive")
        return amount

    def _record(self, kind, amount):
        self.history.append(Transaction(kind, amount, self.balance, datetime.now()))

    def deposit(self, amount):
        amount = self._validate(amount)
        self.balance += amount
        self._record("deposit", amount)
        self._charge("deposit", amount)

    def withdraw(self, amount):
        amount = self._validate(amount)
        fee = self.fee_policy.fee("withdrawal", amount)
        if self.balance - amount - fee < -self.overdraft_limit:
            raise InsufficientFunds(
                f"Insufficient funds: balance {self.balance}, overdraft limit {self.overdraft_limit}")
        self.balance -= amount
        self._record("withdrawal", amount)
        self._charge("withdrawal", amount)

    def _charge(self, kind, amount):
        fee = self.fee_policy.fee(kind, amount)
        if fee > 0:
            self.balance -= fee
            self._record("fee", fee)

    def apply_interest(self):
        interest = self.interest_policy.interest(self.balance)
        if interest > 0:
            self.balance += interest
            self._record("interest", interest)
        return interest


class CheckingAccount(Account):
    type_name = "Checking"


class SavingsAccount(Account):
    type_name = "Savings"


class PremiumAccount(Account):
    type_name = "Premium"
