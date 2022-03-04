from itertools import product
from locale import currency
from proyecto.drivers import factory_driver
from proyecto.pages.home_page import HomePage
from proyecto.utils import data_handler
import pytest

driver = None

def setup():
    global driver
    driver = factory_driver.get_driver()

def test_click_currency():
    currency = HomePage(driver)
    currency.currency_change()
    currency.take_screenshot()

def teardown():
    home_page = HomePage(driver)
    home_page.close_browser()