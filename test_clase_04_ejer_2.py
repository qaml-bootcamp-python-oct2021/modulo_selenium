from typing import ItemsView
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import selenium_driver
import time


driver : WebDriver = None

def setup():
    global driver
    browser = 'chrome'
    driver = selenium_driver.get_driver(browser)
    return driver

def test_search():
    url = 'https://laboratorio.qaminds.com/'
    driver.get(url) 
    driver.maximize_window()
    time.sleep(1)


    tablet_element : WebElement = driver.find_element(By.XPATH, '//ul//a[text() = "Tablets"]')
    assert tablet_element.is_displayed(),'No se encuentra el elemento'
    tablet_element.click()
    time.sleep(2)

    tablet_img : WebElement = driver.find_element(By.XPATH, '//img[@title="Samsung Galaxy Tab 10.1"]')
    assert tablet_img.is_displayed(), 'No se encuentra la imagen'
    tablet_img.click()
    time.sleep(3)

    cost_item : WebElement = driver.find_element(By.XPATH, '//ul//h2[text() = "$241.99"]')
    assert cost_item.is_displayed(), 'El valor es incorrecto'

    wish_item : WebElement = driver.find_element(By.XPATH, '//div//button[@data-original-title="Add to Wish List"]')
    assert wish_item.is_displayed(), 'No se puede agregar a la wishlist'
    wish_item.click()

    add_item_cart : WebElement = driver.find_element(By.XPATH, '//div//button[@id="button-cart"]')
    assert add_item_cart.is_displayed(), 'No se puede agregar el producto al carrito'
    add_item_cart.click()

    time.sleep(3)

def teardown():
    driver.quit()