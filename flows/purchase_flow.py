from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.base_page import BasePage

class PurchaseFlow(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def go_to_cart(self):

        inventory = InventoryPage(self.page)
        inventory.inventory_to_cart()

    def go_to_checkout(self):

        self.go_to_cart()

        cart = CartPage(self.page)
        cart.cart_to_checkout()

    def go_to_checkout_overview(self):

        self.go_to_checkout()

        checkout = CheckoutPage(self.page)
        checkout.checkout_one_to_two()