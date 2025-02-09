
import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_selected_item_into_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    login_page.open_url("https://www.saucedemo.com/")
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    assert "inventory" in driver.current_url, "wrong URL"

    inventory_page.click_on_selected_element(inventory_page.BACKPACK_BUTTON)
    inventory_page.click_on_selected_element(inventory_page.BIKE_LIGHTS_BUTTON)
    inventory_page.click_on_selected_element(inventory_page.TSHIRT_BUTTON)
    inventory_page.click_on_cart_icon()

    assert "cart" in driver.current_url, "wrong URL"

    inventory_page.click_on_selected_element(inventory_page.MENU_BUTTON)
    inventory_page.click_on_sidebar_element(inventory_page.MENU_INVENTORY_BUTTON)

    assert "inventory" in driver.current_url, "wrong URL"

    inventory_page.click_on_cart_icon()


