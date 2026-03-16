import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_two_page import CheckoutTwoPage

@pytest.fixture
def logged_page(page):
    login = LoginPage(page)
    login.go_to()
    login.login("standard_user", "secret_sauce")
    return page

@pytest.fixture
def e2e(page):
    login = LoginPage(page)
    login.go_to()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(logged_page)
    inventory.inventory_to_cart()
    cart = CartPage(logged_page)
    cart.cart_to_checkout()

@pytest.fixture
def login_page(page):
    login = LoginPage(page)
    login.go_to()
    return login

@pytest.fixture
def inventory_page(logged_page):
    inventory = InventoryPage(logged_page)
    inventory.bars.click()
    inventory.reset.click()
    return inventory

@pytest.fixture
def cart_page(logged_page):
    inventory = InventoryPage(logged_page)
    inventory.inventory_to_cart()
    return CartPage(logged_page)

@pytest.fixture
def checkout_page(logged_page):
    inventory = InventoryPage(logged_page)
    inventory.inventory_to_cart()
    cart = CartPage(logged_page)
    cart.cart_to_checkout()
    return CheckoutPage(logged_page)

@pytest.fixture
def checkout_two_page(logged_page):
    inventory = InventoryPage(logged_page)
    inventory.inventory_to_cart()
    cart = CartPage(logged_page)
    cart.cart_to_checkout()
    checkout = CheckoutPage(logged_page)
    checkout.checkout_one_to_two()

