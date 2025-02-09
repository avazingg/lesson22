from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class InventoryPage(BasePage):
    BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    BIKE_LIGHTS_BUTTON = (By.ID, "add-to-cart-sauce-labs-bike-light")
    TSHIRT_BUTTON = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    FLEECE_JACKET_BUTTON = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    ONESIE_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")
    RED_SWEATER = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")

    BACKPACK_REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    BIKE_LIGHTS_REMOVE_BUTTON = (By.ID, "remove-sauce-labs-bike-light")
    TSHIRT_REMOVE_BUTTON = (By.ID, "remove-sauce-labs-bolt-t-shirt")
    FLEECE_JACKET_REMOVE_BUTTON = (By.ID, "remove-sauce-labs-fleece-jacket")
    ONESIE_REMOVE_BUTTON = (By.ID, "remove-sauce-labs-onesie")
    RED_SWEATER_REMOVE_BUTTON = (By.ID, "remove-test.allthethings()-t-shirt-(red)")

    MENU_BUTTON = (By.CLASS_NAME, "bm-burger-button")
    MENU_INVENTORY_BUTTON = (By.ID, "inventory_sidebar_link")

    INVENTORY_CART = (By.ID, "shopping_cart_container")

    def click_on_selected_element(self, element):
        self.click_element(element)

    def click_on_cart_icon(self):
        self.click_element(self.INVENTORY_CART)

    def click_on_sidebar_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()