from typing import ItemsView
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import selenium_driver
import chrome_driver , firefox_driver

def get_driver (browser):
    if browser == 'chrome':
        driver = chrome_driver.create_driver()
    elif browser == 'firefox':
        driver = firefox_driver.create_driver()
    else:
        raise RuntimeError("No existe el driver del navegador indicado")
    return driver