# User Stories — Banking Transaction Management

## Account Management

**US-01 — Create Account**
As a bank teller,
I want to create a new checking or savings account for a customer,
So that the customer can begin depositing funds.

*Acceptance criteria:*
- Account is created with a unique ID, owner name, account type, and a zero starting balance.
- Account type must be either `checking` or `savings`; any other value is rejected.
- Owner name cannot be blank.

---

**US-02 — View Account Details**
As a bank customer,
I want to retrieve my account details by account ID,
So that I can verify my account information.

*Acceptance criteria:*
- Returns account ID, owner name, balance, account type, and active status.
- Returns an error if the account ID does not exist.

---

**US-03 — Close Account**
As a bank teller,
I want to close a customer account,
So that the account is marked inactive and no further transactions are allowed.

*Acceptance criteria:*
- Account must have a zero balance before it can be closed.
- Attempting to close an account with a non-zero balance returns an error.
- Closed account remains in the system but is marked inactive.

---

**US-04 — List Active Accounts**
As a bank manager,
I want to see a list of all active accounts,
So that I can review the current customer base.

*Acceptance criteria:*
- Returns only accounts where `is_active` is `True`.
- Returns an empty list if no active accounts exist.

---

## Transactions

**US-05 — Deposit Funds**
As a bank customer,
I want to deposit money into my account,
So that my balance increases by the deposited amount.

*Acceptance criteria:*
- Deposit amount must be greater than zero.
- Balance is updated immediately.
- A transaction record is created with type `deposit`, timestamp, and description.
- Depositing into an inactive account is rejected.

---

**US-06 — Withdraw Funds**
As a bank customer,
I want to withdraw money from my account,
So that I can access my funds.

*Acceptance criteria:*
- Withdrawal amount must be greater than zero.
- Withdrawal is rejected if the amount exceeds the current balance (no overdraft).
- A transaction record is created with type `withdrawal`.
- Withdrawing from an inactive account is rejected.

---

**US-07 — Transfer Funds**
As a bank customer,
I want to transfer money from one of my accounts to another account,
So that I can move funds without visiting a branch.

*Acceptance criteria:*
- Transfer amount must be greater than zero.
- Source account must have sufficient funds.
- If either the source or destination account does not exist, the transfer is rejected.
- The transfer is atomic: either both accounts are updated or neither is.
- A transaction record is created for both the source account (type `transfer`) and the destination account.
- Transferring to or from an inactive account is rejected.

---

**US-08 — View Transaction History**
As a bank customer,
I want to view a list of all transactions on my account,
So that I can reconcile my statement.

*Acceptance criteria:*
- Returns all transactions for the given account ID.
- Results are sorted by timestamp, most recent first.
- Returns an empty list if no transactions exist for the account.
- Returns an error if the account ID does not exist.
