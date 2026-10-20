import pytest

from inventory import Inventory, Item
from sample_data import build_sample_inventory


def test_add_and_get():
    inv = Inventory()
    inv.add_item(Item("X1", "Widget", "Misc", 5, 2.0))
    assert inv.get("X1").name == "Widget"


def test_duplicate_sku_rejected():
    inv = Inventory()
    inv.add_item(Item("X1", "Widget", "Misc", 5, 2.0))
    with pytest.raises(ValueError):
        inv.add_item(Item("X1", "Other", "Misc", 1, 1.0))


def test_update_quantity_cannot_go_negative():
    inv = build_sample_inventory()
    with pytest.raises(ValueError):
        inv.update_quantity("C301", -5)


def test_total_value():
    inv = Inventory()
    inv.add_item(Item("X1", "Widget", "Misc", 2, 10.0))
    inv.add_item(Item("X2", "Gadget", "Misc", 1, 5.5))
    assert inv.total_value() == pytest.approx(25.5)


def test_find_by_name_is_case_insensitive():
    inv = build_sample_inventory()
    assert [i.sku for i in inv.find_by_name("MOUSE")] == ["A100"]
