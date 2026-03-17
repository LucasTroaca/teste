from .base_page import BasePage
from config.config import URLS
from playwright.sync_api import expect
class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.zip = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.title = page.locator(".title")
        self.url_checkout_one = URLS["checkout_url"]
        self.url_checkout_two = URLS["checkout_two_url"]

    def checkout_one_to_two(self):
        self.first_name.fill("FirstName")
        self.last_name.fill("LastName")
        self.zip.fill("zip")
        self.continue_button.click()

    def expect_checkout_two(self):
        expect(self.page).to_have_url(self.url_checkout_two)
        expect(self.title).to_have_text("Checkout: Overview")

    def expect_checkout_one(self):
        expect(self.page).to_have_url(self.url_checkout_one)
