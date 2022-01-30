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
url = 'https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html'

def setup():
    global driver
    browser = 'chrome'
    driver = selenium_driver.get_driver(browser)
    driver.maximize_window()
    driver.get(url) 


def test_alert_message():

    alert_message: WebElement = driver.find_element(By.ID, 'autoclosable-btn-success')
    assert alert_message.is_displayed() , 'No se encuentra el boton'
    alert_message.click()

    disabled_alert_message = (By.XPATH, '//button[text()="disabled"]')
    driver_w : WebDriverWait = WebDriverWait (driver, 10)
    driver_w.until(ec.visibility_of_element_located(disabled_alert_message))

def teardown():
    driver.quit()