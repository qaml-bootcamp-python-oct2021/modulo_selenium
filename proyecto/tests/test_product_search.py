from proyecto.drivers import factory_driver
from proyecto.pages.home_page import HomePage
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
    home_page.take_screenshot()
    
def teardown():
    home_page = HomePage(driver)
    home_page.close_browser()