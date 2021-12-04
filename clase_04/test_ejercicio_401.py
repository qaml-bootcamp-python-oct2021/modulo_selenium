from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium_driver
import time
import pytest

#ejercicio clase 4_01 - buscar iphone en la barra de busqueda

driver : WebDriver = None

def setup():
    global driver
    browser = 'chrome'
    driver = selenium_driver.get_driver(browser)
    url = 'https://laboratorio.qaminds.com/'
    driver.get(url)

@pytest.mark.qaminds
def test_iphone_search():
    producto = "iphone"
    time.sleep(2)
    driver.maximize_window()
    search_bar : WebElement = driver.find_element(By.XPATH,'//input[@name="search"]')
    assert search_bar.is_displayed(), 'No se encuentra la barra de busqueda'
    search_bar.send_keys(producto)
    search_bar.send_keys(Keys.ENTER)
    time.sleep(2)
    iphone_img : WebElement = driver.find_element(By.XPATH,f'//img[contains(@src,"{producto}")]')
    assert iphone_img.is_displayed(), f'No se encuentra la imagen del producto \'{producto}\''
    time.sleep(2)

def teardown():
    driver.quit()