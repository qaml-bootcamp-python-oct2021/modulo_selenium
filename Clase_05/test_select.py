from typing import ItemsView
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import selenium_driver
import time

driver : WebDriver = None

def setup():
    global driver
    browser = 'chrome'
    driver = selenium_driver.get_driver(browser)
    return driver

def test_search():
    url = 'https://demoqa.com/select-menu'
    driver.maximize_window()
    driver.get(url) 

    select_value : WebElement = driver.find_element(By.XPATH, '//input[@id="react-select-2-input"]')
    assert select_value.is_displayed(), 'No se encuentra el elemento'
    select_value.click()
    time.sleep(2)

def teardown():
    driver.quit()    
