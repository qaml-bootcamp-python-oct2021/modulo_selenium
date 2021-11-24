from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import pytest

driver :WebDriver = None


def setup():
    global driver
    driver=get_driver()
    driver.maximize_window()
    url_pag ='https://laboratorio.qaminds.com/'
    driver.get(url_pag)

def get_driver():
    chrome_driver_path = 'driver/chromedriver'
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    return driver

def test_iphone():
    producto  = 'iphone'
    input_search = driver.find_element(By.CSS_SELECTOR,'#search > input')
    assert input_search.is_displayed(), 'No se encuentra el campo de search'
    input_search.send_keys(producto)
    button_search = driver.find_element(By.CSS_SELECTOR,'#search > input')
    assert button_search.is_displayed(), 'No se encuentra el boton'
    button_search.click()
    imagen_iphone = driver.find_element(By.XPATH, '//img[@alt="iPhone"]')
    assert imagen_iphone.is_displayed(),'No se encuentra la imagen del producto'
    imagen_iphone.click()

def teardown():
    driver.quit()