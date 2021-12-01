
from selenium.webdriver import Chrome


def create_driver():
    driver_path = '../drivers/chromedriver.exe'
    driver = Chrome(executable_path=driver_path)
    return driver