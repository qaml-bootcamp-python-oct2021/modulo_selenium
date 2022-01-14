from proyecto.drivers import factory_driver
from proyecto.pages.home_page import HomePage
from proyecto.pages.search_page import SearchPage
from proyecto.pages.product_page import ProductPage
from proyecto.pages.login_page import LoginPage
from proyecto.utils import data_handler
import time
import pytest

driver = None

def setup():
    global driver
    driver = factory_driver.get_driver()
    
def test_producto_cat_vacia():
    search_page = ProductPage(driver)
    search_page.category_bar()
    search_page.subcat_bar()
    search_page.cat_vacia_error()
    search_page.take_screenshot()
    time.sleep(2)

def teardown():
    home_page = HomePage(driver)
    home_page.close_browser()