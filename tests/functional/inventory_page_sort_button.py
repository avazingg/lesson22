# import pytest
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_sort_button_hilo(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    login_page.valid_login()
    sort_hilo = inventory_page.select_sort_dropdown("hilo")
    assert  sort_hilo == [{'title': 'Sauce Labs Fleece Jacket', 'price': '$49.99'},
                             {'title': 'Sauce Labs Backpack', 'price': '$29.99'},
                             {'title': 'Sauce Labs Bolt T-Shirt', 'price': '$15.99'},
                             {'title': 'Test.allTheThings() T-Shirt (Red)', 'price': '$15.99'},
                             {'title': 'Sauce Labs Bike Light', 'price': '$9.99'},
                             {'title': 'Sauce Labs Onesie', 'price': '$7.99'}], "sorted incorrectly"

def test_sort_button_lohi(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    login_page.valid_login()
    sort_hilo = inventory_page.select_sort_dropdown("lohi")
    assert  sort_hilo == [{'title': 'Sauce Labs Onesie', 'price': '$7.99'},
                          {'title': 'Sauce Labs Bike Light', 'price': '$9.99'},
                          {'title': 'Sauce Labs Bolt T-Shirt', 'price': '$15.99'},
                          {'title': 'Test.allTheThings() T-Shirt (Red)', 'price': '$15.99'},
                          {'title': 'Sauce Labs Backpack', 'price': '$29.99'},
                          {'title': 'Sauce Labs Fleece Jacket', 'price': '$49.99'},], "sorted incorrectly"
    driver.screenshot(path="screenshots/sort_lohi.png")
def test_sort_button_za(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    login_page.valid_login()
    sort_hilo = inventory_page.select_sort_dropdown("za")
    assert  sort_hilo == [{'title': 'Test.allTheThings() T-Shirt (Red)', 'price': '$15.99'},
                          {'title': 'Sauce Labs Onesie', 'price': '$7.99'},
                          {'title': 'Sauce Labs Fleece Jacket', 'price': '$49.99'},
                          {'title': 'Sauce Labs Bolt T-Shirt', 'price': '$15.99'},
                          {'title': 'Sauce Labs Bike Light', 'price': '$9.99'},
                          {'title': 'Sauce Labs Backpack', 'price': '$29.99'},
                          ], "sorted incorrectly"
    driver.screenshot(path="screenshots/sort_az.png")