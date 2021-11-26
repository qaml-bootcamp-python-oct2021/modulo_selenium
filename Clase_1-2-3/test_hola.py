from selenium import webdriver
import time
import pytest

driver = None

def setup():
    global driver
    browser = 'chrome'
    if browser == 'chrome':
        driver_path = './drivers/chromedriver'
        driver = webdriver.Chrome(executable_path=driver_path)
    elif browser == 'firefox':
        driver_path = './drivers/geckodriver'
        driver = webdriver.Firefox(executable_path=driver_path)
    else:
        raise RuntimeError('No existe')

def test_open_qamind():
    url = 'https://qaminds.com/#/'
    driver.get(url)
    time.sleep(5)

def test_open_youtbe():
    url = 'https://youtube.com'
    driver.get(url)
    time.sleep(5)

def teardown():
    driver.quit()