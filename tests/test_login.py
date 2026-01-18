# from pages.login_page import LoginPage
# import time
# PASSWORD = "secret_sauce"

# def test_valid_logins(driver):
#     login = LoginPage(driver)
#     valid_users = [
#         "standard_user",
#         "problem_user",
#         "performance_glitch_user",
#         "error_user",
#         "visual_user"
#     ]

#     for user in valid_users:
#         login.login(user, PASSWORD)
#         time.sleep(5)
#         assert "inventory" in driver.current_url, f"{user} should login successfully"
#         driver.get("https://www.saucedemo.com")  # go back to login for next user

# def test_locked_out_user(driver):
#     login = LoginPage(driver)
#     login.login("locked_out_user", PASSWORD)
#     error = login.get_error_message()
#     assert "locked out" in error.lower()

import pytest
from pages.login_page import LoginPage

PASSWORD = "secret_sauce"

test_users = [
    ("standard_user", True),
    ("problem_user", True),
    ("performance_glitch_user", True),
    ("error_user", True),
    ("visual_user", True),
    ("locked_out_user", False),
]

@pytest.mark.parametrize("username, should_login", test_users)
def test_login_each_user(driver, username, should_login):
    login = LoginPage(driver)
    login.login(username, PASSWORD)

    if should_login:
        assert "inventory" in driver.current_url, f"{username} should login successfully"
    else:
        error = login.get_error_message()
        assert "locked out" in error.lower(), f"{username} should be locked out"

    driver.get("https://www.saucedemo.com")
