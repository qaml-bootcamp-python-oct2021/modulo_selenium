from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver

DRIVER_PATH = './drivers/geckodriver.exe'

def create_driver() -> WebDriver:
    driver = webdriver.Firefox(executable_path=DRIVER_PATH)
    return driver