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
    url_pag ='https://laboratorio.qaminds.com/'
    driver.maximize_window()
    driver.implicitly_wait(1)
    driver.get(url_pag)


def test_search_iphone():
    search_input: WebElement = driver.find_element(By.XPATH, '//div[@id="search"]//input')
    assert search_input.is_displayed, 'No se encuentra el elemento  barra de  busqueda'
    search_input.send_keys('Iphone')

    search_button: WebElement = driver.find_element(By.XPATH, '//div[@id="search"]//button')
    assert search_button.is_displayed, 'No se encuentra el elemento  botón de busqueda'
    search_button.click()
    right_item = 'iPhone'
    wrong_item = 'Samsumg'
    image_finded: WebElement = driver.find_element(By.XPATH, f'//img[@title="{wrong_item}"]')
    assert image_finded.is_displayed, 'No se encontro imagen de producto'
    image_finded.click()

def teardown():
    driver.quit()