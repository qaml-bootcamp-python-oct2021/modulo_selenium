
from selenium.webdriver import Chrome
from selenium.webdriver import Chrome, ChromeOptions
import clase_10.util.config_handler as config
INCOGNITO ='incognito'
HEADLESS ='headless'
def create_driver():
    driver_path =config.get_driver()
    chrome_options = ChromeOptions()
    if config.get_incognite_mode():
        chrome_options.add_argument(INCOGNITO)
    if config.get_headless_enabled():
        chrome_options.add_argument(HEADLESS)
  
    driver = Chrome(options = chrome_options, executable_path=driver_path)
    return driver