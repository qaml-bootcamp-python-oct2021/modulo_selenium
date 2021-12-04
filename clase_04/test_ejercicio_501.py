from attr import attrs
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium_driver
import time
import pytest

driver : WebDriver = None

def setup():
    global driver
    browser = 'chrome'
    driver = selenium_driver.get_driver(browser)
    url = 'https://demoqa.com/select-menu'
    driver.get(url)

@pytest.mark.qaminds
def test_root_option():
    option = "A root option"
    time.sleep(2)
    driver.maximize_window()
    dropdown : WebElement = driver.find_element(By.ID,"withOptGroup")
    assert dropdown.is_displayed(), 'No se encuentra primer dropdown'
    dropdown.click()
    a_root_option : WebElement = driver.find_element(By.XPATH,f'//*[text()="{option}"]')
    assert a_root_option.is_displayed(), f'No se encuentra opcion "{option}"'
    a_root_option.click()
    time.sleep(5)
    

def teardown():
    driver.quit()