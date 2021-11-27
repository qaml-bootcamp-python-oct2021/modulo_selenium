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

def test_tablet_search():
    url = 'https://laboratorio.qaminds.com/'
    #Si encuentra el elemento se ejecuta de inmediato, sino se espera 5 segundos.
    driver.implicitly_wait(5)
    driver.get(url) 
    driver.maximize_window()

    search_bar : WebElement = driver.find_element(By.XPATH, '//div[@id="search"]//input')
    assert search_bar.is_displayed() , 'No se encuentra la barra de busqueda'
    search_bar.send_keys('iPhone')
    search_button : WebElement = driver.find_element(By.XPATH, '//div[@id="search"]//button')
    assert search_button.is_displayed() , 'No se encuentra el boton de busqueda'
    search_button.click()
    image_iphone : WebElement = driver.find_element(By.XPATH, '//a[text()="Samsung"]')
    assert image_iphone.is_displayed() , 'El nombre es incorrecto'

def teardown():
    driver.quit()