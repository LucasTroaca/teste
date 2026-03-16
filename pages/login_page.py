from playwright.sync_api import expect

class LoginPage:
    def __init__(self, page):
        #login-------------------------------
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.log_button = page.locator("#login-button")
        self.error_button = page.locator(".error-message-container.error")
        self.title = page.locator(".title")
        #urls----------------------------------
        self.url_inventory = "https://www.saucedemo.com/inventory.html"
        self.url_cart = "https://www.saucedemo.com/cart.html"
        self.url_checkout_one = "https://www.saucedemo.com/checkout-step-one.html"
        self.url_checkout_two = "https://www.saucedemo.com/checkout-step-two.html"
        #errors--------------------------------
        self.error_message_password = "Epic sadface: Password is required"
        self.error_message_username = "Epic sadface: Username is required"
        self.error_message_credentials = "Epic sadface: Username and password do not match any user in this service"

    def go_to(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.log_button.click()
        
    #meotodos para expect-----------------------------------
    def expect_login_success(self):
        expect(self.page).to_have_url(self.url_inventory)
        expect(self.title).to_have_text("Products")

    def expect_error_credentials(self):
        expect(self.error_button).to_be_visible()
        expect(self.error_button).to_have_text(self.error_message_credentials)

    def expect_error_username(self):
        expect(self.error_button).to_be_visible()
        expect(self.error_button).to_have_text(self.error_message_username)

    def expect_error_password(self):
        expect(self.error_button).to_be_visible()
        expect(self.error_button).to_have_text(self.error_message_password)    
    #screenshot---------------------------------------
    
    def screenshot(self, nome):
        return self.page.screenshot(path=f"screenshots/{nome}")