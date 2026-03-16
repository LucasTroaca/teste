from .base_page import BasePage
from config.config import URLS
from playwright.sync_api import expect

class LoginPage:
    def __init__(self, BasePage):
        self.username = BasePage.locator("#user-name")
        self.password = BasePage.locator("#password")
        self.log_button = BasePage.locator("#login-button")
        self.error_message = BasePage.locator(".error-message-container.error")
        self.title = BasePage.locator(".title")
        self.url_inventory = URLS["inventory_url"]
        self.error_message_password = "Epic sadface: Password is required"
        self.error_message_username = "Epic sadface: Username is required"
        self.error_message_credentials = "Epic sadface: Username and password do not match any user in this service"

    def go_to(self):
        self.BasePage.goto(URLS["base_url"])

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.log_button.click()
        
    #meotodos para expect-----------------------------------
    def expect_login_success(self):
        expect(self.BasePage).to_have_url(self.url_inventory)
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
    #screenshot---------------------------------------
    
    def screenshot(self, name):
        return self.BasePage.screenshot(path=f"screenshots/{name}")