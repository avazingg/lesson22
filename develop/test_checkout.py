import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckOutPage

def test_checkout_witout_any_data(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckOutPage(driver)

    login_page.valid_login()
    inventory_page.click_on_selected_element(inventory_page.BACKPACK_BUTTON)
    inventory_page.click_on_cart_icon()

    cart_page.click_element(cart_page.CHECKOUT_BUTTON)

    assert "checkout" in driver.current_url, "oooopsie, it's supposed to be checkout page"

    checkout_page.click_element(checkout_page.SUBMIT_BUTTON)

    assert driver.find_element(By.CLASS_NAME, "error-message-container").get_attribute("textContent") == "Error: First Name is required"