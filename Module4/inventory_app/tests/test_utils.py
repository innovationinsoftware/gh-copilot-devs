from utils import format_currency


def test_format_currency_two_decimals():
    assert format_currency(1234.5) == "$1,234.50"


def test_format_currency_small_amount():
    assert format_currency(9.99) == "$9.99"
