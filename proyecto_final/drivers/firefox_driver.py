
from selenium.webdriver import Firefox ,FirefoxProfile
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from  proyecto_final.util import config_init
from proyecto_final.util.config_handler import ConfigHadler 
import proyecto_final.util.constants as constants

def create_driver ():
        config: ConfigHadler = config_init.get_config()
        service = Service(config.get_firefox_driver())
        options = Options()
        options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
        options.headless = config.get_headless_enabled()
       
        if config.get_incognite_mode():
                options.add_argument(constants.FIREFOX_PRIVATE);
       
        driver = Firefox(options=options, service=service)
        return driver