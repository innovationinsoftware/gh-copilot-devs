from abc import ABC, abstractmethod
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def money(value) -> Decimal:
    return Decimal(value).quantize(CENT, rounding=ROUND_HALF_UP)


class FeePolicy(ABC):
    @abstractmethod
    def fee(self, kind: str, amount: Decimal) -> Decimal:
        """Fee charged for a transaction of the given kind ('deposit' or 'withdrawal')."""


class InterestPolicy(ABC):
    @abstractmethod
    def interest(self, balance: Decimal) -> Decimal:
        """Interest earned for one period on the given balance."""


class FlatFeePolicy(FeePolicy):
    def __init__(self, deposit_fee="0", withdrawal_fee="0"):
        self._fees = {"deposit": money(deposit_fee), "withdrawal": money(withdrawal_fee)}

    def fee(self, kind, amount):
        return self._fees.get(kind, Decimal("0.00"))


class RateInterestPolicy(InterestPolicy):
    def __init__(self, rate="0"):
        self.rate = Decimal(rate)

    def interest(self, balance):
        return money(balance * self.rate) if balance > 0 else Decimal("0.00")
