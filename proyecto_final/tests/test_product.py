
from time import sleep
import pytest
import proyecto_final.drivers.factory_driver as factory_driver


from proyecto_final.pages.home_page import HomePage
from proyecto_final.pages.product_page import ProductPage
from proyecto_final.pages.search_page import SearchPage

import proyecto_final.util.data_handler as data
import proyecto_final.util.constants as constants
import time

home_page: HomePage = None
search_page: SearchPage = None
product_page: ProductPage = None
def setup():
    driver=  factory_driver.get_driver()
    global home_page 
    home_page = HomePage(driver)
    global product_page 
    product_page = ProductPage(driver)
    global search_page 
    search_page = SearchPage(driver)
  

@pytest.mark.parametrize('product, unit', [('MacBook', '999000999000999000999')])
def test_add_to_car(product, unit):
    home_page.search_producto(product)
    search_page.go_detail_product_found(product)
    product_page.verify_title_page(product,constants.EVIDENCE_PRODUCT)
    product_page.write_quantity(unit)
    product_page.add_to_car()
    product_page.verify_quantity(unit)
    product_page.take_screenshot(constants.EVIDENCE_PRODUCT, f'add_to_car_{product}')
  

def teardown():
    product_page.close_browser()

