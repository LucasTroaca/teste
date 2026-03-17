from .base_page import BasePage
from config.config import URLS
from playwright.sync_api import expect
class CheckoutTwoPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.finish = page.locator("#finish")
        self.cancel = page.locator("#cancel")
        self.back_home_button = page.locator("#back-to-products")
        self.thank_you = page.locator(".complete-header")
        self.finish_url = URLS["finish_url"]

    def end_purchase(self):
        self.finish.click()

    def expect_end_purchase(self):
        expect(self.page).to_have_url(self.finish_url) 
        expect(self.back_home_button).to_be_visible()
        expect(self.thank_you).to_be_visible()