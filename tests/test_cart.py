import pytest

def test_buy_item(cart_page):
    cart_page.click_checkout()
    cart_page.expect_checkout()
