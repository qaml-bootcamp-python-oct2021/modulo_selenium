from proyecto_final.drivers import factory_driver
from proyecto_final.pages.home_page import HomePage
from proyecto_final.pages.product_page import ProductPage
from proyecto_final.pages.search_page import SearchPage
from proyecto_final.utils import data_handler
import pytest


driver = None

def setup():
    global driver
    driver = factory_driver.get_driver()

@pytest.mark.parametrize('product',data_handler.get_data_lines('./proyecto_final/dataset/search_product.csv'))
def test_sarch_product(product):
    home = HomePage(driver)
    home.buscar_producto(product)
    search_page = SearchPage(driver)
    search_page.verify_search_page()
    search_page.take_screenshot()
    search_page.click_on_product(product)
    product_page = ProductPage(driver)
    product_page.verify_product_page(product)
    product_page.take_screenshot()
    home.click_logo()
    home.verify_home_page()

def teardown():
    HomePage(driver).close_browser()