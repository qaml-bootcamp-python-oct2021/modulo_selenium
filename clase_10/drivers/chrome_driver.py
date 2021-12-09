from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome import options
from clase_10.utils import config_handler

INCOGNITO = 'incognito'
HEADLESS = 'headless'

def create_driver():
    options = ChromeOptions()
    if config_handler.get_incognito_mode():
        options.add_argument(INCOGNITO)
    if config_handler.get_headless_mode():
        options.add_argument(HEADLESS)

    driver = Chrome(options=options,executable_path=config_handler.get_driver_path())
    return driver