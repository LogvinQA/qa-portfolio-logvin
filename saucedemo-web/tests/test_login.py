import pytest
from .pages.login_page import LoginPage
from .pages.inventory_page import InventoryPage

VALID_USER = "standard_user"
VALID_PASS = "secret_sauce"

@pytest.mark.ui
def test_success_login(page):
    login = LoginPage(page)
    inv = InventoryPage(page)

    login.open()
    login.login(VALID_USER, VALID_PASS)
    page.wait_for_url("**/inventory.html")
    assert inv.is_open(), "Inventory page title should be 'Products'"

@pytest.mark.ui
@pytest.mark.parametrize("user, pwd, expected", [
    ("locked_out_user", VALID_PASS, "Sorry, this user has been locked out."),
    ("", VALID_PASS, "Username is required"),
    (VALID_USER, "", "Password is required"),
    ("no_such_user", "bad", "Username and password do not match"),
])
def test_negative_login(page, user, pwd, expected):
    login = LoginPage(page)
    login.open()
    login.login(user, pwd)
    assert expected.lower() in login.error_text().lower()
