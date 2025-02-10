import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_cart_items(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.valid_login()

    assert "inventory" in driver.current_url, "wrong URL"

    inventory_page.click_on_selected_element(inventory_page.BACKPACK_BUTTON)
    inventory_page.click_on_selected_element(inventory_page.BIKE_LIGHTS_BUTTON)
    inventory_page.click_on_selected_element(inventory_page.TSHIRT_BUTTON)
    inventory_page.click_on_cart_icon()

    cart_page.selected_element_exists(cart_page.BACKPACK_REMOVE_BUTTON)
    cart_page.selected_element_exists(cart_page.BIKE_LIGHTS_REMOVE_BUTTON)
    cart_page.selected_element_exists(cart_page.TSHIRT_REMOVE_BUTTON)


def test_cart_items_add_and_remove(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.valid_login()

    assert "inventory" in driver.current_url, "wrong URL"

    inventory_page.click_on_selected_element(inventory_page.BACKPACK_BUTTON)
    inventory_page.click_on_selected_element(inventory_page.BIKE_LIGHTS_BUTTON)
    inventory_page.click_on_selected_element(inventory_page.TSHIRT_BUTTON)
    inventory_page.click_on_cart_icon()

    cart_page.selected_element_exists(cart_page.BACKPACK_REMOVE_BUTTON)
    cart_page.selected_element_exists(cart_page.BIKE_LIGHTS_REMOVE_BUTTON)
    cart_page.selected_element_exists(cart_page.TSHIRT_REMOVE_BUTTON)

    inventory_page.click_on_selected_element(inventory_page.MENU_BUTTON)
    inventory_page.click_on_sidebar_element(inventory_page.MENU_INVENTORY_BUTTON)

    inventory_page.click_on_selected_element(inventory_page.BACKPACK_REMOVE_BUTTON)
    inventory_page.click_on_cart_icon()

    cart_page.selected_element_exists(cart_page.BIKE_LIGHTS_REMOVE_BUTTON)
    cart_page.selected_element_exists(cart_page.TSHIRT_REMOVE_BUTTON)
    cart_page.selected_element_does_not_exists(cart_page.BACKPACK_REMOVE_BUTTON)


