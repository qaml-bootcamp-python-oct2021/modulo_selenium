import time
import pytest

import selenium_driver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

driver :WebDriver = None
def setup():
    global driver
    driver = selenium_driver.get_driver()
    url_pag ='https://www.qamindslab.com/#/'
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(url_pag)

def test_close_modal():
    modal : WebElement =  driver.find_element(By.XPATH, '//div[@role="dialog"]')
    assert modal.is_displayed, 'No existe el modal'
    close_modal : WebElement = driver.find_element(By.XPATH, '//button[ @data-testid= "close-button"]' )
    assert close_modal.is_displayed, 'No existe el botón de cierre'
   # close_modal.click()
    logo : WebElement = driver.find_element(By.XPATH, '//img[@alt="logo"]')
    assert logo.is_displayed , 'Modal no cerrado '

  
def teardown():
    driver.quit()
