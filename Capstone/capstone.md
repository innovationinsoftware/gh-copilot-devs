# Copilot Capstone — Banking Transaction Management

Welcome to the Copilot for Developers capstone project. In this project you will build a set of Python banking endpoint functions and unit tests for a transaction management library. There is no database on the VM, so there is no requirement to persist data — mocks are sufficient for data access.

You will use everything you have learned: **chat**, **inline completions**, **prompt files**, **instruction files**, and optionally **skills or hooks**. The goal is to practice using Copilot as a development partner, not just an autocomplete engine.

The user stories are in `user_stories.md`.

> **Note for students:** Two of the tasks below require you to author a Copilot instruction file and a prompt file from scratch. These are real deliverables — not boilerplate to copy. Writing them is how you practice shaping Copilot's behaviour for a team.

---

## Project Structure

Create a new folder on C: root and the following files inside a `C:\Capstone\banking\` folder. Do not use the gh-copilot-devs folder to create this project:

```
Capstone/
  banking/
    models.py          # Account and Transaction data classes
    accounts.py        # Account management endpoints
    transactions.py    # Transaction endpoints
    test_accounts.py   # Unit tests for accounts
    test_transactions.py  # Unit tests for transactions
  .github/
    instructions/
      banking-secure.instructions.md   # Task 2
    prompts/
      new-endpoint.prompt.md           # Task 3
```

---

## Tasks

Work through the tasks in order. Each task has a time estimate to help you pace yourself.

---

### Task 1 — Explore and Plan  *(~20 minutes)*

1. Read `user_stories.md` fully before writing any code.
2. Open Copilot Chat and ask it to suggest a folder and file structure for the project based on the user stories.
3. Ask Copilot to explain what data models you will need (`Account`, `Transaction`).
4. Use the plan to create the empty files listed in the Project Structure section above.

**Goal:** Understand the scope before touching code.

---

### Task 2 — Create the Secure Banking Instruction File  *(~25 minutes)*

**Your task:** Author `.github/instructions/banking-secure.instructions.md` yourself.

This instruction file will tell Copilot how to write **secure banking code** every time it generates endpoint functions in this project. Once it exists, Copilot will follow its rules automatically whenever it touches `accounts.py` or `transactions.py`.

To get started, use Copilot Chat to brainstorm what rules a secure banking library should enforce, then write the instruction file based on that discussion. At minimum your file must establish rules covering:

- How monetary amounts must be typed (think about floating-point precision problems in financial software).
- What input validation every function must perform, and what exception to raise.
- How to handle insufficient funds and inactive accounts.
- What atomicity means for a transfer, and how to guarantee it.
- What must **not** appear in log messages or exception messages (think about data exposure).
- What every function's docstring must contain.
- How many test cases each function requires, and what kinds.

Set the `applyTo` front-matter field so the rules apply automatically to `accounts.py` and `transactions.py`.

**Verify it works:** Ask Copilot to generate a simple `get_balance` function while `accounts.py` is open and confirm the output follows your rules (e.g., uses the correct type for money, includes a docstring, raises the right exception).

---

### Task 3 — Create the New-Endpoint Prompt File  *(~25 minutes)*

**Your task:** Author `.github/prompts/new-endpoint.prompt.md` yourself.

This prompt file is a reusable template that any developer on the team can run to scaffold a new banking endpoint consistently. Think about what information Copilot needs from the developer each time, and what output it should always produce.

Design your prompt so that when it is run it:

1. Collects the endpoint's name, purpose, parameters, and return value from the developer (use template variables or a fill-in-the-blanks section).
2. Produces a function signature with full type hints.
3. Produces a complete docstring.
4. Produces input validation that raises the correct exception.
5. Produces a mock data-access call (no real database).
6. Produces a unit test file section with a happy path test and two failure tests.

Make the prompt reinforce the secure coding rules from Task 2 — either by referencing the instruction file explicitly or by restating the key rules inside the prompt itself.

**Verify it works:** Open the Copilot Chat prompt picker (`/`), run your prompt, and use it to scaffold the `create_account` endpoint. Confirm the output matches the pattern you specified.

---

### Task 4 — Convert User Stories to Gherkin Scenarios  *(~25 minutes)*

**Your task:** Use Copilot to translate every user story in `user_stories.md` into Gherkin Given-When-Then scenarios, then save the output as `Capstone/banking/scenarios.md`.

1. Open `user_stories.md` and add it to the chat context with `#file`.
2. Ask Copilot to convert each user story into one or more Gherkin scenarios using the `Given / When / Then` format. Each acceptance criterion should map to at least one scenario.
3. Review the generated scenarios. Ask Copilot to add any missing **negative scenarios** (e.g., overdraft, inactive account, invalid input) that are implied by the acceptance criteria but not explicitly stated.
4. Save the final set of scenarios to `Capstone/banking/scenarios.md`.

You will use these scenarios as the specification for your unit tests in Task 8. A test should exist for every scenario.

**Example shape of a scenario:**
```gherkin
Scenario: Withdraw funds successfully
  Given an active checking account with a balance of 500.00
  When the customer withdraws 200.00
  Then the account balance is 300.00
  And a withdrawal transaction record is created

Scenario: Withdraw fails due to insufficient funds
  Given an active checking account with a balance of 100.00
  When the customer attempts to withdraw 200.00
  Then a ValueError is raised
  And the account balance remains 100.00
```

---

### Task 5 — Implement the Data Models  *(~20 minutes)*

Open `banking/models.py` and use Copilot to generate the following dataclasses:

- `Account` — fields: `account_id` (str), `owner_name` (str), `balance` (Decimal), `account_type` (str, one of `"checking"` or `"savings"`), `is_active` (bool).
- `Transaction` — fields: `transaction_id` (str), `account_id` (str), `amount` (Decimal), `transaction_type` (str, one of `"deposit"`, `"withdrawal"`, `"transfer"`), `timestamp` (datetime), `description` (str).

Use `@dataclass` from the standard library. Ask Copilot to also generate a `MockAccountRepository` class with an in-memory dictionary that stores `Account` objects and a `MockTransactionRepository` for `Transaction` objects.

---

### Task 6 — Implement Account Endpoints  *(~35 minutes)*

Open `banking/accounts.py`. Use the **new-endpoint prompt** (Task 3) to scaffold each of the following, then refine as needed with inline completions:

| Function | Description |
|---|---|
| `create_account(owner_name, account_type)` | Creates and returns a new `Account` with a generated UUID and a zero balance. |
| `get_account(account_id)` | Returns the `Account` for the given ID, or raises `ValueError` if not found. |
| `close_account(account_id)` | Sets `is_active = False`. Raises `ValueError` if balance is not zero or account not found. |
| `list_accounts()` | Returns a list of all active accounts. |

Each function receives a repository instance as its first parameter so it can be tested with a mock.

---

### Task 7 — Implement Transaction Endpoints  *(~40 minutes)*

Open `banking/transactions.py`. Use the **new-endpoint prompt** to scaffold each of the following:

| Function | Description |
|---|---|
| `deposit(account_id, amount, description)` | Adds `amount` to the account balance. Returns the new `Transaction`. |
| `withdraw(account_id, amount, description)` | Subtracts `amount` from balance. Raises `ValueError` if insufficient funds. |
| `transfer(from_account_id, to_account_id, amount, description)` | Moves `amount` between accounts atomically. |
| `get_transaction_history(account_id)` | Returns a list of all transactions for the account, sorted by timestamp descending. |

---

### Task 8 — Write Unit Tests from Gherkin Scenarios  *(~35 minutes)*

Open `test_accounts.py` and `test_transactions.py`. Add `scenarios.md` to the chat context with `#file` and ask Copilot to generate a `unittest` test method for **every scenario** in the file.

Each generated test should:
- Be named after the scenario (e.g., `test_withdraw_fails_due_to_insufficient_funds`).
- Follow the Arrange / Act / Assert structure that mirrors the Given / When / Then from the scenario.
- Use a fresh `MockAccountRepository` and `MockTransactionRepository` created in `setUp`.

After generation, verify that every scenario in `scenarios.md` has a corresponding test method. Ask Copilot to identify any gaps.

Run the tests and fix any failures with Copilot's help.

---

### Task 9 — Review and Harden  *(~20 minutes)*

1. Ask Copilot Chat: *"Review `transactions.py` against the banking-secure instruction file and identify any gaps."* Fix any issues it finds.
2. Ask Copilot to generate a brief `README.md` inside the `banking/` folder that describes the library, its functions, and how to run the tests.
3. Verify all tests pass with `python -m pytest Capstone/banking/` (or `python -m unittest discover`).

---

## Completion Checklist

- [ ] `banking-secure.instructions.md` created and applied to endpoint files
- [ ] `new-endpoint.prompt.md` created and used to scaffold at least one endpoint
- [ ] User stories converted to Gherkin scenarios and saved to `scenarios.md`
- [ ] Negative/edge-case scenarios added to `scenarios.md`
- [ ] All four account endpoints implemented and tested
- [ ] All four transaction endpoints implemented and tested
- [ ] Every function uses `Decimal` for monetary values
- [ ] Every function validates inputs and raises `ValueError`
- [ ] Transfer is atomic
- [ ] Every Gherkin scenario has a corresponding unit test
- [ ] All tests pass
- [ ] `banking/README.md` generated

---

## Tips

- Use **`/` in Copilot Chat** to pick your prompt file.
- Use **`#codebase`** to give Copilot context about existing code before asking it to generate something new.
- If a generated function doesn't match the secure coding rules, paste the rule into chat and ask Copilot to revise.
- Use **inline chat** (`Ctrl+I`) inside a file when you want a targeted change without leaving the editor.

