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
expected_price = '122'

def setup():
    global driver
    driver = factory_driver.get_driver()

def test_search():
    desk_element : WebElement = driver.find_element(By.XPATH,'//li//a[text() = "Desktops"]')
    assert desk_element.is_displayed(), 'No se encuentra el elemento'
    desk_element.click()
    
    click_windows : WebElement = driver.find_element(By.XPATH, '//li//a[text() = "Mac (1)"]')
    assert click_windows.is_displayed(), 'No se encuentra el elemento'
    click_windows.click()

    title_imac : WebElement = driver.find_element(By.XPATH, '//h4//a[text() = "iMac"]')
    assert title_imac.is_displayed(), 'No se encuentra el producto'
    title_imac.click()

    add_cart_button : WebElement = driver.find_element (By.ID, 'button-cart')
    assert add_cart_button.is_displayed(), 'No se encuentra el boton'
    add_cart_button.click()


    driver_w : WebDriverWait = WebDriverWait (driver, 10)
    locator_modal = (By.XPATH, f'//span[@id = "cart-total" and contains(text(), "{expected_price}")]' )
    button : WebElement = driver_w.until(ec.visibility_of_element_located(locator_modal))

    driver.save_screenshot('./ejercicio_02.png')

def teardown():
    driver.quit()