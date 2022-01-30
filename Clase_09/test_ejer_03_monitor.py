from typing import ItemsView
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.remote import webelement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import factory_driver
import time

driver : WebDriver = None
expected_price = '189.87'

def setup():
    global driver
    driver = factory_driver.get_driver()

def test_shopping_monitor():
    search_display : WebElement = driver.find_element(By.XPATH, '//span[text() = "Currency"]')
    assert search_display.is_displayed() , 'No se encuentra el elemento'
    search_display.click()

    select_currency : WebElement = driver.find_element(By.XPATH, '//button[text() = "$ US Dollar"]')
    assert select_currency.is_displayed(), 'No se encuentra el elemento'
    select_currency.click()

    search_monitor : WebElement = driver.find_element(By.XPATH, '//div[@id="search"]//input')
    assert search_monitor.is_displayed(), 'No se encuentra la barra de busqueda'
    search_monitor.send_keys('Samsung')

    search_button : webelement = driver.find_element(By.XPATH, '//div[@id="search"]//button')
    assert search_button.is_displayed(), 'No se encuentra el boton de busqueda'
    search_button.click()

    select_monitor : WebElement = driver.find_element(By.XPATH, '//a[text() = "Samsung SyncMaster 941BW"]')
    assert select_monitor.is_displayed(), 'No se encuentra el producto'
    select_monitor.click()

    search_display : WebElement = driver.find_element(By.XPATH, '//span[text() = "Currency"]')
    assert search_display.is_displayed() , 'No se encuentra el elemento'
    search_display.click()

    select_currency : WebElement = driver.find_element(By.XPATH, '//button[text() = "€ Euro"]')
    assert select_currency.is_displayed(), 'No se encuentra el elemento'
    select_currency.click()

    add_cart_button : WebElement = driver.find_element (By.ID, 'button-cart')
    assert add_cart_button.is_displayed(), 'No se encuentra el boton'
    add_cart_button.click()
    
    driver_w : WebDriverWait = WebDriverWait (driver, 10)
    locator_modal = (By.XPATH, f'//span[@id = "cart-total" and contains(text(), "{expected_price}")]' )
    button : WebElement = driver_w.until(ec.visibility_of_element_located(locator_modal))

    time.sleep(2)
    
def teardown():
    driver.quit()    