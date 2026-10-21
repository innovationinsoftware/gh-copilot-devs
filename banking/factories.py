from abc import ABC, abstractmethod

from accounts import Account, CheckingAccount, PremiumAccount, SavingsAccount
from policies import FeePolicy, FlatFeePolicy, InterestPolicy, RateInterestPolicy


class AccountFactory(ABC):
    """Abstract factory: creates a matching family of account, fee policy and interest policy."""

    @abstractmethod
    def create_account(self, number: str, owner: str) -> Account: ...

    @abstractmethod
    def create_fee_policy(self) -> FeePolicy: ...

    @abstractmethod
    def create_interest_policy(self) -> InterestPolicy: ...


class CheckingFactory(AccountFactory):
    def create_account(self, number, owner):
        return CheckingAccount(number, owner, self.create_fee_policy(),
                               self.create_interest_policy(), overdraft_limit="500")

    def create_fee_policy(self):
        return FlatFeePolicy(withdrawal_fee="1.00")

    def create_interest_policy(self):
        return RateInterestPolicy("0")


class SavingsFactory(AccountFactory):
    def create_account(self, number, owner):
        return SavingsAccount(number, owner, self.create_fee_policy(),
                              self.create_interest_policy(), overdraft_limit="0")

    def create_fee_policy(self):
        return FlatFeePolicy(withdrawal_fee="2.50")

    def create_interest_policy(self):
        return RateInterestPolicy("0.02")


class PremiumFactory(AccountFactory):
    def create_account(self, number, owner):
        return PremiumAccount(number, owner, self.create_fee_policy(),
                              self.create_interest_policy(), overdraft_limit="5000")

    def create_fee_policy(self):
        return FlatFeePolicy()

    def create_interest_policy(self):
        return RateInterestPolicy("0.035")


FACTORIES = {
    "checking": CheckingFactory,
    "savings": SavingsFactory,
    "premium": PremiumFactory,
}
