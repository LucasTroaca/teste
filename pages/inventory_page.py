from .base_page import BasePage
from playwright.sync_api import expect
from data.products_data import BACKPACK

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.open_menu = page.locator("#react-burger-menu-btn")
        self.filter = page.locator(".product_sort_container")
        self.cart_button = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.reset = page.locator("#reset_sidebar_link")

    def inventory_to_cart(self):
        self.open_menu.click()
        self.reset.click()
        self.add_product(BACKPACK)
        self.cart_button.click()

    def add_product(self, product):
        self.page.click(f"#add-to-cart-sauce-labs-{product}")

    def expect_add(self, product):
        expect(self.page.locator(f"#remove-sauce-labs-{product}")).to_be_visible()

    def remove_product(self, product):
        self.page.click(f"#remove-sauce-labs-{product}")
    
    def expect_remove(self, product):
        expect(self.page.locator(f"#add-to-cart-sauce-labs-{product}")).to_be_visible()
    
    def expect_cart(self, value):
        expect(self.cart_badge).to_have_text(value)

    def selected_filter(self, option):
        self.filter.select_option(option)

    def get_product_names(self):
        names = self.page.locator(".inventory_item_name").all_text_contents()
        return names
    
    def get_products_price(self):
        prices = self.page.locator(".inventory_item_price").all_text_contents()
        return prices