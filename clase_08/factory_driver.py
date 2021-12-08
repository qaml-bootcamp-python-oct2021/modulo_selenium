from selenium import webdriver
import firefox_driver
import chrome_driver
import config_handler
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