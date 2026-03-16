import pytest
from playwright.sync_api import expect

class CartPage:
    def __init__(self, page):
        self.page = page
        self.checkout = page.locator("#checkout")
        self.continue_shopping = page.locator("#continue-shopping")
        self.url_checkout = "https://www.saucedemo.com/checkout-step-one.html"

    def checkout_click(self):
        self.checkout.click()

    def expect_checkout(self):
        expect(self.page).to_have_url(self.url_checkout)

    def cart_to_checkout(self):
        self.checkout_click()
        self.expect_checkout()
        