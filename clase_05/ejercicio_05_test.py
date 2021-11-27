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
    url_pag ='https://demoqa.com/select-menu'
    driver.get(url_pag)
    driver.maximize_window()
    

def test_select_option():
    global driver
    select: WebElement = driver.find_element(By.ID, 'withOptGroup')
    assert select.is_displayed, 'No se encuentra select'
    select.click()
    option_data = 'A root option'
    xpath_option =f'//*[text()="{option_data}"]'
    option: WebElement = driver.find_element(By.XPATH, xpath_option )
    option.click()
   

def teardown():
    driver.quit()

 

    
    

