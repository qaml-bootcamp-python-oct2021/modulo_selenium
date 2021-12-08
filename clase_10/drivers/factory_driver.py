from selenium import webdriver
from clase_10.drivers import firefox_driver
from clase_10.drivers import chrome_driver
from clase_10.util import config_handler
FIREFOX= 'firefox'
CHROME= 'chrome'
def get_driver():
    config_handler.load_config()
    browser = config_handler.get_browser()
    if browser == FIREFOX:
        driver = firefox_driver.create_driver()
    elif browser == CHROME:
        driver = chrome_driver.create_driver()
    else:
        raise Exception('No found driver')
    if not config_handler.get_headless_enabled():
        driver.maximize_window()
    
    driver.get(config_handler.get_url())

    return driver