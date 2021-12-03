from selenium.webdriver import Chrome, ChromeOptions
import config_handler

INCOGNITO = 'incognito'
HEADLESS = 'headless'

def create_driver():
    chrome_options = ChromeOptions()
    if config_handler.get_incognito_mode():
        chrome_options.add_argument(INCOGNITO)
    if config_handler.get_headless_mode():
        chrome_options.add_argument(HEADLESS)
    driver = Chrome(options=chrome_options,executable_path=config_handler.get_driver_path())

    return driver
