import pytest
from pages.checkout_two_page import CheckoutTwoPage


def test_end_of_purchase(checkout_two_page):
    checkout_two_page.end_purchase()
    checkout_two_page.expect_end_purchase()
    checkout_two_page.back_home_button.click()


