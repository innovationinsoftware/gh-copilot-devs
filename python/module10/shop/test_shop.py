from shop import Shopper, Item
import unittest

class TestShop(unittest.TestCase):

    def test_loyalty_discount_applied(self):
        # Boundary test: Verify loyalty discount is applied correctly
        shopper = Shopper(loyalty_points=100)
        shopper.add_to_cart(Item(price=100))
        final_price = shopper.checkout()
        self.assertEqual(final_price, 90, "Loyalty discount not applied correctly")

        # Negative test: Verify no discount is applied for ineligible shoppers
        shopper = Shopper(loyalty_points=0)
        shopper.add_to_cart(Item(price=100))
        final_price = shopper.checkout()
        self.assertEqual(final_price, 100, "Discount applied incorrectly")

    def test_order_history(self):
        # Boundary test: Verify order history updates correctly
        shopper = Shopper()
        shopper.add_to_cart(Item(price=50))
        shopper.checkout()
        history = shopper.get_order_history()
        self.assertEqual(len(history), 1, "Order history not updated correctly")

        # Negative test: Verify empty order history for new shoppers
        shopper = Shopper()
        history = shopper.get_order_history()
        self.assertEqual(len(history), 0, "Order history should be empty")

    def test_wishlist_functionality(self):
        # Boundary test: Verify items can be added to wishlist
        shopper = Shopper()
        item = Item(price=30)
        shopper.add_to_wishlist(item)
        self.assertIn(item, shopper.get_wishlist(), "Item not added to wishlist")

        # Negative test: Verify wishlist is empty for new shoppers
        shopper = Shopper()
        self.assertEqual(len(shopper.get_wishlist()), 0, "Wishlist should be empty")

if __name__ == "__main__":
    unittest.main()