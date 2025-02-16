# from selenium.webdriver.common.by import By
#
# from pages.base_page import BasePage
#
# class CartPage(BasePage):
#     BACKPACK_REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")
#     BIKE_LIGHTS_REMOVE_BUTTON = (By.ID, "remove-sauce-labs-bike-light")
#     TSHIRT_REMOVE_BUTTON = (By.ID, "remove-sauce-labs-bolt-t-shirt")
#     FLEECE_JACKET_REMOVE_BUTTON = (By.ID, "remove-sauce-labs-fleece-jacket")
#     ONESIE_REMOVE_BUTTON = (By.ID, "remove-sauce-labs-onesie")
#     RED_SWEATER_REMOVE_BUTTON = (By.ID, "remove-test.allthethings()-t-shirt-(red)")
#     CHECKOUT_BUTTON = (By.ID, "checkout")
#
#     def selected_element_exists(self, element):
#         assert self.find_element(element), f"no {element} located on the page"
#     def selected_element_does_not_exists(self, element):
#         assert self.find_element(element, timeout=2) is None, f"Unexpected {element} located on the page"

from pages.base_page import BasePage

class CartPage(BasePage):
    BACKPACK_REMOVE_BUTTON = "#remove-sauce-labs-backpack"
    BIKE_LIGHTS_REMOVE_BUTTON = "#remove-sauce-labs-bike-light"
    TSHIRT_REMOVE_BUTTON = "#remove-sauce-labs-bolt-t-shirt"
    FLEECE_JACKET_REMOVE_BUTTON = "#remove-sauce-labs-fleece-jacket"
    ONESIE_REMOVE_BUTTON = "#remove-sauce-labs-onesie"
    RED_SWEATER_REMOVE_BUTTON = "#remove-test-allthethings-t-shirt-red"
    CHECKOUT_BUTTON = "#checkout"

    def selected_element_exists(self, element):
        assert self.find_element(element), f"no {element} located on the page"

    def selected_element_does_not_exists(self, element):
        assert self.find_element(element, timeout=2) is None, f"Unexpected {element} located on the page"