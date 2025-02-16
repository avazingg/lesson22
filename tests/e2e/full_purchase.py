import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckOutPage

def test_full_purchase(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckOutPage(driver)
    login_page.valid_login()
    inventory_page.click_on_selected_element(inventory_page.BACKPACK_BUTTON)
    inventory_page.click_on_cart_icon()

    cart_page.click_element(cart_page.CHECKOUT_BUTTON)
    checkout_page.full_checkout_data("Name", "LastName", "1234")
    checkout_page.click_element(checkout_page.SUBMIT_BUTTON)

    assert "checkout-step-two" in  driver.url, "wrong destination, it's supposed to be 2nd step of checkout"
    driver.screenshot(path="screenshots/full_purchase.png")