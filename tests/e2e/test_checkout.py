from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckOutPage

def test_checkout_without_zipcode(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckOutPage(driver)

    login_page.valid_login()

    inventory_page.click_on_selected_element(inventory_page.BACKPACK_BUTTON)
    inventory_page.click_on_cart_icon()

    cart_page.click_element(cart_page.CHECKOUT_BUTTON)

    assert "checkout-step-one" in driver.url, "Неверная страница, должна быть checkout-step-one"

    checkout_page.full_checkout_data("John", "Doe", "")

    checkout_page.click_element(checkout_page.SUBMIT_BUTTON)

    error_element = driver.wait_for_selector(".error-message-container")
    assert error_element.inner_text().strip() == "Error: Postal Code is required", "Неверный текст ошибки"
    driver.screenshot(path="screenshots/checkout_negative.png")