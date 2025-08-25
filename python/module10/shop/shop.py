class Item:
    def __init__(self, price):
        self.price = price


class Shopper:
    def __init__(self, loyalty_points=0):
        self.loyalty_points = loyalty_points
        self.cart = []
        self.order_history = []
        self.wishlist = []

    def add_to_cart(self, item):
        self.cart.append(item)

    def checkout(self):
        total = sum(item.price for item in self.cart)
        if self.loyalty_points >= 100:
            total *= 0.9  # Apply 10% discount
        self.order_history.append(self.cart)
        self.cart = []
        return total

    def get_order_history(self):
        return self.order_history

    def add_to_wishlist(self, item):
        self.wishlist.append(item)

    def get_wishlist(self):
        return self.wishlist
