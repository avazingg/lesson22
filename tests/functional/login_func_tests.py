import pytest

from conftest import driver
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

def test_validation_with_empty_fields(driver):
    login_page = LoginPage(driver)
    login_page.open_url("https://www.saucedemo.com/")
    login_page.enter_username("")
    login_page.enter_password("")
    login_page.click_login()
    assert driver.find_element(By.CLASS_NAME,"error-message-container").get_attribute("textContent") == "Epic sadface: Username is required"

@pytest.mark.parametrize(
    ("name"),[
        ('standard_user'),
        ('locked_out_user'),
        ('problem_user'),
        ('performance_glitch_user'),
    ]
)
def test_validation_with_only_login(driver, name):
    login_page = LoginPage(driver)
    login_page.open_url("https://www.saucedemo.com/")
    login_page.enter_username(name)
    login_page.enter_password("")
    login_page.click_login()
    assert driver.find_element(By.CLASS_NAME,"error-message-container").get_attribute("textContent") == "Epic sadface: Password is required"

@pytest.mark.parametrize(
    ("password"),[
        ('random_passowrd'),
        ('secret_sauce'),
    ]
)
def test_validation_with_only_password(driver, password):
    login_page = LoginPage(driver)
    login_page.open_url("https://www.saucedemo.com/")
    login_page.enter_username("")
    login_page.enter_password(password)
    login_page.click_login()
    assert driver.find_element(By.CLASS_NAME, "error-message-container").get_attribute(
        "textContent") == "Epic sadface: Username is required"

@pytest.mark.parametrize(
    ("name", "password"),[
        ('wrong_login', "secret_sauce"),
        ('standard_user', "wrong_password"),
    ]
)
def test_validation_with_incorrect_login_or_password(driver, name, password):
    login_page = LoginPage(driver)
    login_page.open_url("https://www.saucedemo.com/")
    login_page.enter_username(name)
    login_page.enter_password(password)
    login_page.click_login()
    assert driver.find_element(By.CLASS_NAME, "error-message-container").get_attribute(
        "textContent") == "Epic sadface: Username and password do not match any user in this service"