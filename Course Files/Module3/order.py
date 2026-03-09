class Order:
    """
    Represents a customer order.

    Attributes:
        order_id (str): Order identifier.
        items (list[str]): Ordered items.
        total_amount (float): Order total.
        status (str): Current status.
    """

    def __init__(self, order_id: str, items: list[str], total_amount: float):
        self.order_id = order_id
        self.items = items
        self.total_amount = total_amount
        self.status = "pending"

    def calculate_total(self, tax_rate: float) -> float:
        """Return total amount including tax."""
        return self.total_amount * (1 + tax_rate)

…
