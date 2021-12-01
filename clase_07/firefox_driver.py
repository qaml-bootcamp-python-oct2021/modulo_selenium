from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox


def create_driver ():
        driver_path = '../drivers/geckodriver.exe'
        options = Options()
        options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
        driver = Firefox(options=options,executable_path=driver_path)
        return driver