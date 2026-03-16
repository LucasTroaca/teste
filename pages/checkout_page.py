from .base_page import BasePage
from config.config import URLS
from playwright.sync_api import expect
class CheckoutPage:
    def __init__(self, BasePage):
        self.first_name = BasePage.locator("#first-name")
        self.last_name = BasePage.locator("#last-name")
        self.zip = BasePage.locator("#postal-code")
        self.continue_button = BasePage.locator("#continue")
        self.title = BasePage.locator(".title")
        self.url_checkout_one = URLS["checkout_url"]
        self.url_checkout_two = URLS["checkout_two_url"]

    def checkout_one_to_two(self):
        self.first_name.fill("FirstName")
        self.last_name.fill("LastName")
        self.zip.fill("zip")
        self.continue_button.click()

    def expect_checkout_two(self):
        expect(self.BasePage).to_have_url(self.url_checkout_two)
        expect(self.title).to_have_text("Checkout: Overview")

    def expect_checkout_one(self):
        expect(self.BasePage).to_have_url(self.url_checkout_one)
