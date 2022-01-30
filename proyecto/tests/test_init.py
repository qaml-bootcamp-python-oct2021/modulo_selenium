from proyecto.drivers import factory_driver
from proyecto.pages.home_page import HomePage


driver = None

def setup():
    global driver
    driver = factory_driver.get_driver()
    
def test_init():
    home_page = HomePage(driver)
    home_page.click_logo()
    home_page.take_screenshot()

def teardown():
    home_page = HomePage(driver)
    home_page.close_browser()
