from typing import ItemsView
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.remote import webelement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import factory_driver
import time


driver : WebDriver = None

def setup():
    global driver
    driver = factory_driver.get_driver()

def test_search():

    search_display : WebElement = driver.find_element(By.XPATH, '//div[@id="search"]//input')
    assert search_display.is_displayed() , 'No se encuentra la barra de busqueda'
    search_display.send_keys('display')
    
    search_button : webelement = driver.find_element(By.XPATH, '//div[@id="search"]//button')
    assert search_button.is_displayed() , 'No se encuentra el boton de busqueda'
    search_button.click()

    checkbox_descriptions : WebElement = driver.find_element(By.XPATH, '//input[@id = "description"]')
    assert checkbox_descriptions.is_displayed(), 'No se encuentra el checkbox'
    checkbox_descriptions.click()

    search_button : WebElement = driver.find_element(By.XPATH, '//input[@id = "button-search"]')
    assert search_button.is_displayed(), 'No se encuentra el boton'
    search_button.click()

    driver.save_screenshot('./ejercicio_01.png')

def teardown():
    driver.quit()