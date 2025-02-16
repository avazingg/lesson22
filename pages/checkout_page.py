from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckOutPage(BasePage):
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    POSTAL_CODE = "#postal-code"
    SUBMIT_BUTTON = ".submit-button"
    CANCEL_BUTTON = "#cancel"

    def enter_first_name(self, firstname):
        self.enter_text(self.FIRST_NAME, firstname)

    def enter_last_name(self, lastname):
        self.enter_text(self.LAST_NAME, lastname)

    def enter_post_code(self, postcode):
        self.enter_text(self.POSTAL_CODE, postcode)

    def full_checkout_data(self, firstname, lastname, postcode):
        self.enter_first_name(firstname)
        self.enter_last_name(lastname)
        self.enter_post_code(postcode)

