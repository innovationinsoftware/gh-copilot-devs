from pathlib import Path

BASE = Path(__file__).parent
OUT = BASE / "invitations"
OUT.mkdir(exist_ok=True)

TEMPLATE = """Hi {first}!

You're invited to a birthday party! 🎉

When: Saturday at 3 PM
Where: 12 Oak Street

There will be cake, games, and lots of fun. We'd love for you to be there!

See you Saturday!
"""

count = 0
for line in (BASE / "guests.txt").read_text(encoding="utf-8").splitlines():
    name = line.strip()
    if not name:
        continue
    first = name.split()[0]
    filename = "_".join(name.split()) + ".txt"
    (OUT / filename).write_text(TEMPLATE.format(first=first), encoding="utf-8")
    count += 1

print(f"Created {count} invitations in {OUT}")
