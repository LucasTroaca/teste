from pages.checkout_page import CheckoutPage

def test_finish_purchase(checkout_page):
    checkout_page.expect_checkout_one()
    checkout_page.checkout_one_to_two()
    checkout_page.expect_checkout_two()

