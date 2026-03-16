from .base_page import BasePage
from config.config import URLS
from playwright.sync_api import expect
class CheckoutTwoPage:
    def __init__(self, BasePage):
        self.finish = BasePage.locator("#finish")
        self.cancel = BasePage.locator("#cancel")
        self.back_home_button = BasePage.locator("#back-to-products")
        self.thank_you = BasePage.locator(".complete-header")
        self.finish_url = URLS["finish_url"]

    def end_purchase(self):
        self.finish.click()

    def expect_end_purchase(self):
        expect(self.BasePage).to_have_url(self.finish_url) 
        expect(self.back_home_button).to_be_visible()
        expect(self.thank_you).to_be_visible()