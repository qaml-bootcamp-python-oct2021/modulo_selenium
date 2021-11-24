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

def test_search_iphone():
    global driver
    url_pag ='https://laboratorio.qaminds.com/'
    driver.get(url_pag)
    current_url= driver.current_url
    assert url_pag == current_url, f'Url no coinciden,  actual:{current_url} buscada:{url_pag}'
    search_input: WebElement = driver.find_element(By.XPATH, '//div[@id="search"]//input')
    assert search_input.is_displayed, 'No se encuentra el elemento  barra de  busqueda'
    search_input.send_keys('Iphone')

    search_button: WebElement = driver.find_element(By.XPATH, '//div[@id="search"]//button')
    assert search_button.is_displayed, 'No se encuentra el elemento  botón de busqueda'
    search_button.click()
    
    image_finded: WebElement = driver.find_element(By.XPATH, '//img[@title="iPhone"]')
    assert image_finded.is_displayed, 'No se encontro imagen de producto'
    image_finded.click()

def teardown():
    driver.quit()