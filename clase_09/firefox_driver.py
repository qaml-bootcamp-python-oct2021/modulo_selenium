from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
import config_handler


def create_driver ():
        driver_path = config_handler.get_driver()
        options = Options()
        options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
        driver = Firefox(options=options,executable_path=driver_path)
        return driver