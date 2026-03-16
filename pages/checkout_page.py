import pytest
from playwright.sync_api import expect

class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.zip = page.locator("#postal-code")
        self.continue_buy = page.locator("#continue")
        self.url_checkout_two = "https://www.saucedemo.com/checkout-step-one.html"
        self.title = page.locator(".title")

    def checkout_one_to_two(self):
        self.first_name.fill("FirstName")
        self.last_name.fill("LastName")
        self.zip.fill("zip")
        self.continue_buy.click()

    def expect_checkout_one(self):
        expect(self.page).to_have_url(self.url_checkout_two)
        expect(self.title).to_have_text("Checkout: Your Information")
