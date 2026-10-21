import os
import sys
import unittest
from decimal import Decimal

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from accounts import BankError, InsufficientFunds
from bank import Bank
from factories import CheckingFactory, PremiumFactory, SavingsFactory


class FactoryTests(unittest.TestCase):
    def test_each_factory_builds_its_family(self):
        for f, name in [(CheckingFactory(), "Checking"), (SavingsFactory(), "Savings"),
                        (PremiumFactory(), "Premium")]:
            self.assertEqual(f.create_account("1", "A").type_name, name)

    def test_savings_interest_and_no_overdraft(self):
        b = Bank()
        a = b.open_account("Ann", "savings")
        a.deposit("100")
        with self.assertRaises(InsufficientFunds):
            a.withdraw("100")  # fee pushes below zero
        self.assertEqual(a.apply_interest(), Decimal("2.00"))
        self.assertEqual(a.balance, Decimal("102.00"))

    def test_checking_overdraft_and_fee(self):
        a = CheckingFactory().create_account("1", "Bob")
        a.withdraw("100")
        self.assertEqual(a.balance, Decimal("-101.00"))
        with self.assertRaises(InsufficientFunds):
            a.withdraw("500")

    def test_premium_no_fees(self):
        a = PremiumFactory().create_account("1", "Cy")
        a.deposit("10")
        a.withdraw("10")
        self.assertEqual(a.balance, Decimal("0.00"))


class BankTests(unittest.TestCase):
    def test_transfer(self):
        b = Bank()
        x, y = b.open_account("X", "premium"), b.open_account("Y", "savings")
        x.deposit("50")
        b.transfer(x.number, y.number, "20")
        self.assertEqual((x.balance, y.balance), (Decimal("30.00"), Decimal("20.00")))

    def test_invalid(self):
        b = Bank()
        a = b.open_account("X", "checking")
        for bad in ("0", "-5", "abc"):
            with self.assertRaises(BankError):
                a.deposit(bad)
        with self.assertRaises(BankError):
            b.open_account("X", "gold")
        with self.assertRaises(BankError):
            b.get("nope")
        with self.assertRaises(BankError):
            b.transfer(a.number, a.number, "1")

    def test_statement(self):
        b = Bank()
        a = b.open_account("X", "premium")
        a.deposit("5")
        self.assertIn("Balance: 5.00", b.statement(a.number))


if __name__ == "__main__":
    unittest.main()
