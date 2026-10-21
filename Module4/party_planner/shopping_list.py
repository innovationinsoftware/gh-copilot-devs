import math
import re
from collections import OrderedDict
from pathlib import Path

BASE = Path(__file__).parent
SERVINGS = 4
ROUND_UP = {"eggs", "lemons"}


def count_people():
    lines = (BASE / "guests.txt").read_text(encoding="utf-8").splitlines()
    return len([l for l in lines if l.strip()]) + 1  # +1 for the host


def read_recipes():
    items = []
    for line in (BASE / "recipes.txt").read_text(encoding="utf-8").splitlines():
        m = re.match(r"\s*-\s*(.+?):\s*([\d.]+)\s*(.*)$", line)
        if m:
            items.append((m.group(1).strip(), float(m.group(2)), m.group(3).strip()))
    return items


def fmt(n):
    return str(int(n)) if n == int(n) else f"{n:g}"


def main():
    people = count_people()
    factor = people / SERVINGS
    totals = OrderedDict()
    for name, amount, unit in read_recipes():
        key = (name.lower(), unit)
        totals[key] = totals.get(key, 0) + amount * factor

    out = [f"Shopping list for {people} people (guests + host)", ""]
    for (name, unit), amount in totals.items():
        if name in ROUND_UP:
            amount = math.ceil(round(amount, 9))
        else:
            amount = round(amount, 2)
        out.append(f"- {name}: {fmt(amount)} {unit}".rstrip())

    text = "\n".join(out) + "\n"
    (BASE / "shopping_list.txt").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
