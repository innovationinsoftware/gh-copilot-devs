from accounts import Account, BankError
from factories import FACTORIES, AccountFactory


class Bank:
    def __init__(self):
        self._accounts: dict[str, Account] = {}
        self._next = 1000

    def open_account(self, owner: str, factory: AccountFactory | str) -> Account:
        if isinstance(factory, str):
            try:
                factory = FACTORIES[factory.lower().strip()]()
            except KeyError:
                raise BankError(f"Unknown account type: {factory}") from None
        if not owner.strip():
            raise BankError("Owner name required")
        self._next += 1
        account = factory.create_account(str(self._next), owner.strip())
        self._accounts[account.number] = account
        return account

    def get(self, number: str) -> Account:
        try:
            return self._accounts[number.strip()]
        except KeyError:
            raise BankError(f"Account {number} not found") from None

    def accounts(self):
        return list(self._accounts.values())

    def deposit(self, number, amount):
        self.get(number).deposit(amount)

    def withdraw(self, number, amount):
        self.get(number).withdraw(amount)

    def transfer(self, source, target, amount):
        src, dst = self.get(source), self.get(target)
        if src is dst:
            raise BankError("Cannot transfer to the same account")
        src.withdraw(amount)
        dst.deposit(amount)

    def apply_interest(self):
        return {a.number: a.apply_interest() for a in self._accounts.values()}

    def statement(self, number) -> str:
        acct = self.get(number)
        lines = [f"{acct.type_name} account {acct.number} - {acct.owner}"]
        for t in acct.history:
            lines.append(f"{t.timestamp:%Y-%m-%d %H:%M:%S}  {t.kind:<10} {t.amount:>12}  bal {t.balance_after:>12}")
        lines.append(f"Balance: {acct.balance}")
        return "\n".join(lines)
