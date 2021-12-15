from clase_09.drivers import factory_driver
from clase_09.pages.home_page import HomePage
import time

def test_init():
    driver = factory_driver.get_driver()
    home_page = HomePage (driver)
    time.sleep(3)
    home_page.close_browser()