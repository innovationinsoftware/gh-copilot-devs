"""Small helper functions.

YOUR TASK (do this by hand in the main VS Code window while the agents work):
format_currency has a bug. Run the tests to see it fail, then fix it.
"""


def format_currency(amount: float) -> str:
    """Return an amount like $1,234.50"""
    return f"${amount:,.1f}"
