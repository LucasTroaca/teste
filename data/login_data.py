from pages.login_page import LoginPage

login_test_data = [
    ("standard_user", "secret_sauce", LoginPage.expect_login_success),
    ("wrong_user", "secret_sauce", LoginPage.expect_error_credentials),
    ("standard_user", "wrong_password", LoginPage.expect_error_credentials),
    ("", "secret_sauce", LoginPage.expect_error_username),
    ("standard_user", "", LoginPage.expect_error_password),
    ("", "", LoginPage.expect_error_username),
]