from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium_driver
import pytest

driver : WebDriver = None

url = 'https://laboratorio.qaminds.com/'

def setup():
    global driver
    browser = 'chrome'
    driver = selenium_driver.get_driver(browser)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(url)

@pytest.mark.qaminds
def test_neg_samsung_search():
    #search by iphone, but expecting samsung on the label
    product_entered = "iphone"
    product_expected = "samsung"
    driver.maximize_window()
    search_bar : WebElement = driver.find_element(By.XPATH,'//input[@name="search"]')
    assert search_bar.is_displayed(), 'No se encuentra la barra de busqueda'
    search_bar.send_keys(product_entered)
    search_bar.send_keys(Keys.ENTER)
    product_title : WebElement = driver.find_element(By.XPATH,f'//h4//a[contains(@href,"{product_expected}")]')
    assert product_title.is_displayed(), f'No se encuentra el label de producto \'{product_expected}\''

def teardown():
    driver.quit()