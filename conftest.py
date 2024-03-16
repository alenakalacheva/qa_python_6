import allure
import pytest
from selenium import webdriver

from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.zen_page import ZenPage


@allure.title("Prepare for the test")  # декоратор
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()  # set up
    yield driver
    driver.quit()  # tear down


@pytest.fixture(scope="function")
def main_page(driver):
    return MainPage(driver)

@pytest.fixture(scope="function")
def order_page(driver):
    return OrderPage(driver)

@pytest.fixture(scope="function")
def zen_page(driver):
    return ZenPage(driver)
