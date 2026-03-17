from .base_page import BasePage
from config.config import URLS
from playwright.sync_api import expect

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.log_button = page.locator("#login-button")
        self.error_message = page.locator(".error-message-container.error")
        self.title = page.locator(".title")
        self.url_inventory = URLS["inventory_url"]
        self.error_message_password = "Epic sadface: Password is required"
        self.error_message_username = "Epic sadface: Username is required"
        self.error_message_credentials = "Epic sadface: Username and password do not match any user in this service"

    def go_to(self):
        self.page.goto(URLS["base_url"])

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.log_button.click()
        
    def expect_login_success(self):
        expect(self.page).to_have_url(self.url_inventory)
        expect(self.title).to_have_text("Products")

    def expect_error_credentials(self):
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_have_text(self.error_message_credentials)

    def expect_error_username(self):
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_have_text(self.error_message_username)

    def expect_error_password(self):
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_have_text(self.error_message_password)    
    
    def screenshot(self, name):
        return self.page.screenshot(path=f"screenshots/{name}")