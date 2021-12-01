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
url = 'https://demo.seleniumeasy.com/bootstrap-download-progress-demo.html'

def setup():
    global driver
    browser = 'chrome'
    driver = selenium_driver.get_driver(browser)
    driver.maximize_window()
    driver.get(url) 


def test_download():

    down_button : WebElement = driver.find_element(By.ID, 'cricle-btn')
    assert down_button.is_displayed() , 'No se encuentra el boton'
    down_button.click()

    percentage_message = (By.XPATH, '//div[contains(@class,"circle end complate")]//div[text()="100%"]')
    driver_w : WebDriverWait = WebDriverWait (driver, 10)
    driver_w.until(ec.visibility_of_element_located(percentage_message))
    

def teardown():
    driver.quit()

