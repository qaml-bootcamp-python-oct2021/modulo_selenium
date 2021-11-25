from selenium import webdriver
import time
import pytest

driver = None

def setup():
    global driver
    browser = 'chrome'
    if browser == 'chrome':
        driver_path = './modulo_selenium/driver/chromedriver'
        driver = webdriver.Chrome(executable_path=driver_path)
    elif browser == 'firefox':
        driver_path = './modulo_selenium/driver/geckodriver'
        driver = webdriver.Firefox(executable_path=driver_path)
    else:
        raise RuntimeError('No existe')
    return driver

def test_open_qamind():
    url = 'https://qaminds.com/#/'
    driver.get(url)
    time.sleep(3)

def test_open_youtbe():
    url = 'https://youtube.com'
    driver.get(url)
    time.sleep(3)

def teardown():
    driver.quit()