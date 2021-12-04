from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

DRIVER_PATH = './drivers/chromedriver.exe'

def create_driver() -> WebDriver:
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    return driver