from proyecto_final.drivers import factory_driver
from proyecto_final.pages.home_page import HomePage
import time

driver = factory_driver.get_driver()

def test_init():
    home_page = HomePage(driver)
    home_page.verify_logo()
    home_page.click_logo()
    home_page.take_screenshot()
    

def teardown():
    home_page = HomePage(driver)
    home_page.close_browser()