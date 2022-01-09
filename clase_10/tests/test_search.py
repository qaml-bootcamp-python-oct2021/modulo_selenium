


import clase_10.drivers.factory_driver as factory_driver

import pytest

from clase_10.pages.home_page import HomePage
from clase_10.pages.search_page import SearchPage


home_page: HomePage = None
search_page: SearchPage = None
def setup():
    driver=  factory_driver.get_driver()
    global home_page 
    home_page = HomePage(driver)
    global search_page 
    search_page = SearchPage(driver)

@pytest.mark.parametrize('product_name, img_expected', [('Iphone', 'iPhone'), ('Canon','Canon EOS 5D')])
def test_iphone(product_name, img_expected):
    home_page.search_producto(product_name)
    search_page.go_detail_product_found(img_expected)
   

def teardown():
    home_page.close_browser()

