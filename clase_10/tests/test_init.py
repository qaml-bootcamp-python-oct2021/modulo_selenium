from selenium.webdriver.remote.webdriver import WebDriver
from clase_10.drivers import factory_driver
from clase_10.pages.base_page import BasePage
import pytest

from clase_10.pages.home_page import HomePage

driver : WebDriver = None
page : BasePage = None

def setup():
    global driver, page
    driver = factory_driver.get_driver()
    page = BasePage(driver)

@pytest.mark.ejercicio_01
def test_ejemplo():
    home = HomePage(driver)
    home.verify_logo()
    home.search('iphone')



def teardown():
    page.close_browser()