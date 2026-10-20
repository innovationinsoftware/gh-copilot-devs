# Inventory App: "Open in Agents" Demo

A tiny store inventory project used to show two AI agents working in the
background while you fix a bug by hand.

## Setup

```
pip install pytest
python -m pytest -q
```

You will see **5 passed, 2 failed**. The 2 failures are on purpose (see Step 4).

## Step 1: Open the Agents window

Click **Open in Agents** in the VS Code title bar.

## Step 2: Start Agent Task 1 (save and load data)

Start a new session for this folder and paste:

```
Create a new file storage.py that works with the Inventory class in inventory.py.
Add four functions: save_to_json(inventory, path), load_from_json(path),
export_to_csv(inventory, path), and import_from_csv(path).
import_from_csv must validate every row: skip rows with a missing SKU,
a non-numeric quantity or price, or a negative value, and return both the
Inventory and a list of error messages that include the row number.
Write pytest tests in tests/test_storage.py that use tmp_path, including a
CSV with at least three different kinds of bad rows. Do not change
inventory.py or utils.py. Run the tests and make sure they all pass.
```

## Step 3: Start Agent Task 2 (reports and command line)

Start a second session for the same folder and paste:

```
Create reports.py with three functions that take an Inventory from inventory.py:
low_stock(inventory, threshold=5) returns items at or below the threshold,
sorted by quantity; value_by_category(inventory) returns a dict of
category to total value; top_items(inventory, n=3) returns the n most
valuable items. Then create cli.py using argparse with three subcommands
that run against build_sample_inventory() from sample_data.py:
"list", "low-stock --threshold N", and "report" (prints value by category
and the top 3 items). Write pytest tests in tests/test_reports.py and
tests/test_cli.py (use capsys for the CLI). Do not change inventory.py or
utils.py. Run the tests and make sure they all pass.
```

Both agents are now working at the same time.

## Step 4: Your task (in the main VS Code window)

While the agents work, go back to the main editor window and fix the bug in
`utils.py`. Run the tests to see what is wrong:

```
python -m pytest tests/test_utils.py -q
```

Fix `format_currency`, then run the tests again until they pass.

## Step 5: Review and accept

Go back to the Agents window. For each finished session:

1. Open the session and review the changed files.
2. Ask for changes if something looks wrong.
3. Accept the changes.

Then run everything:

```
python -m pytest -q
python cli.py report
```

## Why the tasks are split this way

- Each agent writes **new files only**, so the two sessions do not conflict.
- Both prompts say "do not change inventory.py or utils.py," so your hand fix
  in `utils.py` does not collide with the agents.
- Both prompts end with "run the tests," so the agents check their own work,
  which also makes each task take a few minutes.
