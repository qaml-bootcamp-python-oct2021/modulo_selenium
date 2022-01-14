from proyecto.drivers import factory_driver
from proyecto.pages.home_page import HomePage
from proyecto.pages.search_page import SearchPage
from proyecto.utils import data_handler
import time
import pytest

driver = None

def setup():
    global driver
    driver = factory_driver.get_driver()
    
@pytest.mark.parametrize('producto',data_handler.get_data('./proyecto/dataset/buscar_producto.csv'))
def test_buscar_prod(producto):
    home_page= HomePage(driver)
    home_page.buscar_producto(producto)
    search_page = SearchPage(driver)
    home_page.take_screenshot()
    time.sleep(2)

def teardown():
    home_page = HomePage(driver)
    home_page.close_browser()