import time
import pytest

import selenium_driver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver :WebDriver = None
def setup():
    global driver
    driver = selenium_driver.get_driver()
    url_pag ='https://demo.seleniumeasy.com/'

    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(url_pag)

def test_close_popup():

    close_popup : WebElement = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "at-cv-lightbox-close")))
    close_popup.click()
 

  
def teardown():
    driver.quit()
