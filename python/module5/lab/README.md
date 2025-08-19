# Lab: Use Copilot to Identify & Resolve Common Coding Errors

This folder contains separate starter files per exercise. Open each in VS Code with GitHub Copilot enabled.


## 0) Setup
1. Open this folder in VS Code.
2. Ensure Copilot is active (status bar icon).
3. Use the terminal in this folder to run each file with `python <filename>`.

---

## Part A — Undefined Variables & Wrong Arguments

### A1 — `part_a1.py`
1. Run `python part_a1.py` and observe the failure.
2. Use Copilot to introduce the missing data so the greeting can be constructed correctly.
3. Re-run until it prints a valid welcome message.

### A2 — `part_a2.py`
1. Run `python part_a2.py` and observe the error.
2. Use Copilot to correct the function call so it supplies appropriate arguments.
3. Re-run and verify the formatted name output looks correct.

---

## Part B — Error Handling: Exceptions vs Proactive Checks

### B1 — `part_b1.py`
1. Create a `grades.txt` file in this folder. Try with it empty; then with some invalid and then valid lines: 90
85
95
100
80
2. Run `python part_b1.py` and note different failure modes.
3. Use Copilot to add robust error handling for file/parse issues and add a safe guard to avoid dividing by zero.
4. Re-run with valid numeric data and verify an average is produced.

---

## Part C — Syntax Fixes

### C1 — `part_c1.py`
1. Run `python part_c1.py` to see syntax failures.
2. Use Copilot to fix all syntax issues and indentation so the program runs.
3. Re-run and verify it prints a message and a small sequence of numbers.

---

## Part D — Debugging Logic

### D1 — `part_d1.py` (Factorial)
1. Run `python part_d1.py` and inspect the output/behavior.
2. Use Copilot to correct the logic so the function returns the correct factorial result.
3. (Optional) Ask Copilot for a non-recursive version to improve efficiency.

### D2 — `part_d2.py` (Fibonacci Sequence)
1. Run `python part_d2.py` and examine the length/content of the output.
2. Use Copilot to adjust the logic so the function returns exactly **n** terms.
3. Re-run and verify the sequence length matches the input.

