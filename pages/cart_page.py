from .base_page import BasePage
from config.config import URLS
from playwright.sync_api import expect
class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.checkout = page.locator("#checkout")
        self.continue_shopping = page.locator("#continue-shopping")
        self.url_checkout = URLS["checkout_url"]

    def checkout_click(self):
        self.checkout.click()

    def expect_checkout(self):
        expect(self.page).to_have_url(self.url_checkout)

    def cart_to_checkout(self):
        self.checkout_click()
        self.expect_checkout()
        