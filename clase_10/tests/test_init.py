


import clase_10.drivers.factory_driver as factory_driver
from clase_10.pages.home_page import HomePage


driver = factory_driver.get_driver()
def setup():
    global driver
    driver =  factory_driver.get_driver()


def test_init():
    home_page = HomePage(driver)
    home_page.verify_logo()

def test_click_logo():
    home_page = HomePage(driver)
    home_page.click_logo()

def teardown():
    home_page = HomePage(driver)
    home_page.close_browser()

