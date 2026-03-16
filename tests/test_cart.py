import pytest

def test_buy_item(cart_page):
    cart_page.checkout_click()
    cart_page.expect_checkout()
