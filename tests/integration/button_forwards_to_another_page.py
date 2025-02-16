import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckOutPage

def test_login_page_login_button(driver):
    login_page = LoginPage(driver)
    login_page.valid_login()
    assert "inventory" in driver.url, "login button doesn't forward us to inventory page"

def test_cart_button(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    login_page.valid_login()
    inventory_page.click_on_selected_element(inventory_page.BACKPACK_BUTTON)
    inventory_page.click_on_cart_icon()
    assert "cart" in driver.url, "cart button doesn't forward us to cart page"

def test_sidebar_logout(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    login_page.valid_login()
    inventory_page.click_element(inventory_page.MENU_BUTTON)
    inventory_page.click_on_sidebar_element(inventory_page.LOGOUT_SIDEBAR_BUTTON)
    assert not "inventory" in driver.url, "button supposed lead to login page"

def test_sidebar_link_to_inventory(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    login_page.valid_login()
    inventory_page.click_on_cart_icon()
    inventory_page.click_element(inventory_page.MENU_BUTTON)
    inventory_page.click_on_sidebar_element(inventory_page.MENU_INVENTORY_BUTTON)
    assert  "inventory" in driver.url, "button supposed lead to inventory page"
