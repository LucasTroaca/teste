import pytest
from playwright.sync_api import expect

class CheckoutTwoPage:
    def __init__(self, page):
        self.page = page
        self.finish = page.locator("#finish")
        self.cancel = page.locator("#cancel")
        self.price_item = page.locator(".inventory_item_price")
        self.url_finish = "https://www.saucedemo.com/checkout-complete.html"
        self.back_home_button = page.locator("#back-to-products")
        self.thank_you = page.locator(".complete-header")

    def end_purchase(self):
        self.finish.click()

    def expect_end_purchase(self):
       expect(self.page).to_have_url(self.url_finish) 
       expect(self.back_home_button).to_be_visible()
       expect(self.thank_you).to_be_visible()