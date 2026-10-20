"""Core inventory model for a small store."""

from dataclasses import dataclass


@dataclass
class Item:
    sku: str
    name: str
    category: str
    quantity: int
    unit_price: float

    @property
    def value(self) -> float:
        return self.quantity * self.unit_price


class Inventory:
    def __init__(self):
        self._items: dict[str, Item] = {}

    def add_item(self, item: Item) -> None:
        if item.sku in self._items:
            raise ValueError(f"SKU already exists: {item.sku}")
        if item.quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if item.unit_price < 0:
            raise ValueError("Price cannot be negative")
        self._items[item.sku] = item

    def remove_item(self, sku: str) -> None:
        if sku not in self._items:
            raise KeyError(f"No item with SKU: {sku}")
        del self._items[sku]

    def update_quantity(self, sku: str, change: int) -> int:
        item = self.get(sku)
        new_qty = item.quantity + change
        if new_qty < 0:
            raise ValueError("Not enough stock")
        item.quantity = new_qty
        return new_qty

    def get(self, sku: str) -> Item:
        if sku not in self._items:
            raise KeyError(f"No item with SKU: {sku}")
        return self._items[sku]

    def find_by_name(self, text: str) -> list[Item]:
        text = text.lower()
        return [i for i in self._items.values() if text in i.name.lower()]

    def all_items(self) -> list[Item]:
        return list(self._items.values())

    def total_value(self) -> float:
        return sum(i.value for i in self._items.values())
