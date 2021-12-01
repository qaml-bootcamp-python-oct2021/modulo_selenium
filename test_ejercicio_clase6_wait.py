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


def test_start_download():
    driver_w : WebDriverWait = WebDriverWait(driver, 5)
    button_download : WebElement = driver.find_element(By.ID, 'downloadButton')
    assert button_download.is_displayed(), "No se encuentra el boton Start Download"
    button_download = driver_w.until(ec.element_to_be_clickable(button_download))
    button_download.click()

    completed_message = (By.XPATH, '//div[@id= "dialog"]/div[text()="Complete!"]')
    driver_w : WebDriverWait = WebDriverWait(driver, 10)
    driver_w.until(ec.visibility_of_element_located(completed_message))
    
    close_button_locator = (By.XPATH, '//button[text()="Close"]')
    driver_w.until(ec.visibility_of_element_located(close_button_locator))
    button_close : WebElement = driver_w.until(ec.element_to_be_clickable(close_button_locator))
    button_close.click()


def teardown():
    driver.quit()