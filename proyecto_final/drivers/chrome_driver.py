
from ast import Constant
from selenium.webdriver import Chrome
from selenium.webdriver import Chrome, ChromeOptions
from  proyecto_final.util import config_init
from proyecto_final.util.config_handler import ConfigHadler 
import proyecto_final.util.constants as constants
def create_driver():
    config : ConfigHadler = config_init.get_config()

    chrome_options = ChromeOptions()
    if config.get_incognite_mode():
        chrome_options.add_argument(constants.CHROME_INCOGNITO)
    if config.get_headless_enabled():
        chrome_options.add_argument(constants.CHROME_HEADLESS)
  
    driver = Chrome(options = chrome_options, executable_path=config.get_chrome_driver())
    return driver