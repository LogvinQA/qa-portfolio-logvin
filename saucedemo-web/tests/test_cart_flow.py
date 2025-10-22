import pytest
from .pages.login_page import LoginPage
from .pages.inventory_page import InventoryPage


@pytest.mark.ui
def test_add_to_cart_and_checkout_visible(page):
    login = LoginPage(page)
    inv = InventoryPage(page)

    login.open()
    login.login("standard_user", "secret_sauce")
    page.wait_for_url("**/inventory.html")

    inv.add_first_n_items(2)
    assert inv.cart_count() == 2

    inv.open_cart()
    assert inv.can_checkout(), "Checkout button should be visible"
