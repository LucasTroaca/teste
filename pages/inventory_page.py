from .base_page import BasePage
from playwright.sync_api import expect
from data.products_data import BACKPACK

class InventoryPage:
    def __init__(self, BasePage):
        self.open_menu = BasePage.locator("#react-burger-menu-btn")
        self.filter = BasePage.locator(".product_sort_container")
        self.cart_button = BasePage.locator(".shopping_cart_link")
        self.cart_badge = BasePage.locator(".shopping_cart_badge")
        self.reset = BasePage.locator("#reset_sidebar_link")

    def inventory_to_cart(self):
        self.open_menu.click()
        self.reset.click()
        self.add_product(BACKPACK)
        self.cart_button.click()

    def add_product(self, product):
        self.BasePage.click(f"#add-to-cart-sauce-labs-{product}")

    def expect_add(self, product):
        expect(self.BasePage.locator(f"#remove-sauce-labs-{product}")).to_be_visible()

    def remove_product(self, product):
        self.BasePage.click(f"#remove-sauce-labs-{product}")
    
    def expect_remove(self, product):
        expect(self.BasePage.locator(f"#add-to-cart-sauce-labs-{product}")).to_be_visible()
    
    def expect_cart(self, value):
        expect(self.cart_badge).to_have_text(value)

    def selected_filter(self, option):
        self.filter.select_option(option)

    def get_product_names(self):
        names = self.BasePage.locator(".inventory_item_name").all_text_contents()
        return names
    
    def get_products_price(self):
        prices = self.BasePage.locator(".inventory_item_price").all_text_contents()
        return prices