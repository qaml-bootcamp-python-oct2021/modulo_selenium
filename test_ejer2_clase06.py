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
url = 'https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html'

def setup():
    global driver
    browser = 'chrome'
    driver = selenium_driver.get_driver(browser)
    driver.maximize_window()
    driver.get(url) 


def test_download():
    #'//textarea[@id="textbox"]'
    enter_data : WebElement = driver.find_element(By.XPATH, '//textarea[@id="textbox"]')
    assert enter_data.is_displayed() , 'No se encuentra el input form'
    enter_data.send_keys('Prueba')

def teardown():
    driver.quit()