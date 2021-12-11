from clase_09.drivers import factory_driver
from clase_09.pages.home_page import HomePage
from clase_09.pages.search_page import SearchPage
import time
import pytest
from clase_09.utils import data_handler

driver = None

def setup():
    global driver
    driver = factory_driver.get_driver()

# def test_init():
#     home_page = HomePage(driver)
#     home_page.click_logo()
#     home_page.take_screenshot()

@pytest.mark.parametrize('producto',data_handler.get_data('./clase_09/dataset/buscar_prod.csv'))
def test_buscar_prod(producto):
    home_page = HomePage(driver)
    home_page.buscar_producto(producto)
    search_page = SearchPage(driver)
    time.sleep(2)
    
@pytest.mark.parametrize('username,password,success',data_handler.get_data('./clase_09/dataset/login.csv'))
def test_login(username,password,success):
    pass

def teardown():
    home_page = HomePage(driver)
    home_page.close_browser()