from typing import ItemsView
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import selenium_driver
import time


driver : WebDriver = None
url = 'https://demo.seleniumeasy.com/'
def setup():
    global driver
    browser = 'chrome'
    driver = selenium_driver.get_driver(browser)
    driver.maximize_window()
    driver.get(url) 

def test_modal_close():
    text_expected = 'No, thanks!'
    driver_w : WebDriverWait = WebDriverWait (driver, 10)
    locator_modal = (By.XPATH, f'//a[text()="{text_expected}"]' )
    button : WebElement = driver_w.until(ec.visibility_of_element_located(locator_modal))
    button.click()

def teardown():
    driver.quit()