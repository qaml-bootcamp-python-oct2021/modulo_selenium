
from selenium.webdriver import Chrome
from selenium.webdriver import Chrome, ChromeOptions
import config_handler
INCOGNITO ='incognito'
HEADLESS ='headless'
def create_driver():
    driver_path =config_handler.get_driver()
    chrome_options = ChromeOptions()
    if config_handler.get_incognite_mode():
        chrome_options.add_argument(INCOGNITO)
    if config_handler.get_headless_enabled():
        chrome_options.add_argument(HEADLESS)
  
    driver = Chrome(options = chrome_options, executable_path=driver_path)
    return driver