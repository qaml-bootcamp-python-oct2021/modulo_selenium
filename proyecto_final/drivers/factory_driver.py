from selenium import webdriver
from proyecto_final.drivers import firefox_driver
from proyecto_final.drivers import chrome_driver
import  proyecto_final.util.config_init  as config_init
FIREFOX= 'firefox'
CHROME= 'chrome'

def get_driver():
    config = config_init.get_config()
    browser = config.get_browser()
    global driver
    if browser == FIREFOX:
        driver = firefox_driver.create_driver()
    elif browser == CHROME:
        driver = chrome_driver.create_driver()
    else:
        raise Exception('No found driver')
    if not config.get_headless_enabled():
        driver.maximize_window()
    
    driver.get(config.get_url())

    return driver