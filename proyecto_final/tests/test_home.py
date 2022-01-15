
from time import sleep
import pytest
import proyecto_final.drivers.factory_driver as factory_driver


from proyecto_final.pages.home_page import HomePage
from proyecto_final.pages.product_page import ProductPage
import proyecto_final.util.data_handler as data
import proyecto_final.util.constants as constants
import time

home_page: HomePage = None
product_page: ProductPage = None
def setup():
    driver=  factory_driver.get_driver()
    global home_page 
    home_page = HomePage(driver)
    global product_page 
    product_page = ProductPage(driver)


@pytest.mark.parametrize('product_name', data.get_data(constants.DATA_PRODUCT))
def test_featured_detail_product(product_name):
    home_page.click_img_featured(product_name)
    home_page.verify_title_page(product_name,constants.EVIDENCE_HOME)
    product_page.verify_header_text_content(product_name)
    product_page.take_screenshot(constants.EVIDENCE_HOME, f'featured_detail_{product_name}')
   

def teardown():
    home_page.close_browser()

