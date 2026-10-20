"""Builds a sample inventory to play with."""

from inventory import Inventory, Item


def build_sample_inventory() -> Inventory:
    inv = Inventory()
    inv.add_item(Item("A100", "Wireless Mouse", "Electronics", 25, 19.99))
    inv.add_item(Item("A101", "USB-C Cable", "Electronics", 3, 9.50))
    inv.add_item(Item("B200", "Notebook", "Stationery", 120, 2.25))
    inv.add_item(Item("B201", "Gel Pen 10-pack", "Stationery", 4, 7.99))
    inv.add_item(Item("C300", "Desk Lamp", "Furniture", 8, 34.00))
    inv.add_item(Item("C301", "Office Chair", "Furniture", 2, 149.00))
    return inv


if __name__ == "__main__":
    from utils import format_currency

    inv = build_sample_inventory()
    for item in inv.all_items():
        print(f"{item.sku}  {item.name:<18} qty={item.quantity:<4} {format_currency(item.value)}")
    print("Total:", format_currency(inv.total_value()))
