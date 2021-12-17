from proyecto_final.drivers import factory_driver
from proyecto_final.pages.home_page import HomePage
import time

def test_init():
    driver = factory_driver.get_driver()
    home_page = HomePage (driver)
    time.sleep(3)
    home_page.close_browser()