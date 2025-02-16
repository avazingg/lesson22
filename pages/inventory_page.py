from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver
from pages.base_page import BasePage

class InventoryPage(BasePage):
    BACKPACK_BUTTON = "#add-to-cart-sauce-labs-backpack"
    BIKE_LIGHTS_BUTTON = "#add-to-cart-sauce-labs-bike-light"
    TSHIRT_BUTTON = "#add-to-cart-sauce-labs-bolt-t-shirt"
    FLEECE_JACKET_BUTTON = "#add-to-cart-sauce-labs-fleece-jacket"
    ONESIE_BUTTON = "#add-to-cart-sauce-labs-onesie"
    RED_SWEATER = "#add-to-cart-test.allthethings()-t-shirt-(red)"
    PRODUCTS =  ".inventory_item"

    BACKPACK_REMOVE_BUTTON =  "#remove-sauce-labs-backpack"
    BIKE_LIGHTS_REMOVE_BUTTON = "#remove-sauce-labs-bike-light"
    TSHIRT_REMOVE_BUTTON =  "#remove-sauce-labs-bolt-t-shirt"
    FLEECE_JACKET_REMOVE_BUTTON =  "#remove-sauce-labs-fleece-jacket"
    ONESIE_REMOVE_BUTTON =  "#remove-sauce-labs-onesie"
    RED_SWEATER_REMOVE_BUTTON =  "#remove-test.allthethings()-t-shirt-(red)"

    MENU_BUTTON = ".bm-burger-button"
    LOGOUT_SIDEBAR_BUTTON = "#logout_sidebar_link"
    MENU_INVENTORY_BUTTON = "#inventory_sidebar_link"
    INVENTORY_CART = "#shopping_cart_container"
    SORT_BUTTON = "select.product_sort_container"

    def click_on_selected_element(self, element):
        self.click_element(element)

    def click_on_cart_icon(self):
        self.click_element(self.INVENTORY_CART)

    def click_on_sidebar_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()

    def select_sort_dropdown(self, value):
        sort_dropdown = self.find_element(self.SORT_BUTTON)
        sort_dropdown.select_option(value)
        products = self.driver.query_selector_all(self.PRODUCTS)
        products_list = []
        for product in products:
            title = product.query_selector(".inventory_item_name").inner_text()
            price = product.query_selector(".inventory_item_price").inner_text()
            products_list.append({"title": title, "price": price})
        return products_list