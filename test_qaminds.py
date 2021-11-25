
from selenium import webdriver
from selenium.webdriver.remote import webelement
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import selenium_driver
import time

driver : webdriver = None

def setup():
    global driver
    browser = 'firefox'
    driver = selenium_driver.get_driver(browser)


def test_open_qamind():
    url = 'https://qamindslab.com/'
    driver.get(url)
    time.sleep(3)

def test_open_youtube():
    url = 'https://youtube.com/'
    driver.get(url)
    time.sleep(3)

def test_open_facebook():
    url = 'https://facebook.com/'
    driver.get(url)
    time.sleep(3)
    

def teardown():
    driver.quit()