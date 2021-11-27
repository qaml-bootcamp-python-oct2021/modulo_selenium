from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pytest

driver : WebDriver = None
url = 'https://demoqa.com/select-menu'

def get_driver():
    global driver
    driver_path = './driver/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)
    
def setup():
    get_driver()
    driver.maximize_window()
    driver.get(url)

def test_select_option():
    option = 'Aqua'
    select : WebElement = driver.find_element(By.ID,'oldSelectMenu')
    assert select.is_displayed() , 'No se encuentra el selector'
    option_list = Select(select)
    option_list.select_by_visible_text(option)
    time.sleep(3)

@pytest.mark.ejercicio05
def test_select_value():
    option = 'A root option'
    select : WebElement = driver.find_element(By.ID,'withOptGroup')
    assert select.is_displayed() , 'No se encuentra el selector'
    select.click()
    time.sleep(3)

def teardown():
    driver.quit()