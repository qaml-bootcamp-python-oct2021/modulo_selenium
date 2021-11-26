from typing import ItemsView
from selenium import webdriver
from selenium.webdriver.common import by
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

    lap_net_element : WebElement = driver.find_element(By.XPATH,'//li//a[text() = "Laptops & Notebooks"]')
    assert lap_net_element.is_displayed(), 'No se encuentra el elemento'
    lap_net_element.click()
    time.sleep(1)

    click_windows : WebElement = driver.find_element(By.XPATH, '//li//a[text() = "Windows (0)"]')
    assert click_windows.is_displayed(), 'No se encuentra el elemento'
    click_windows.click()
    time.sleep(2)

    cost_item : WebElement = driver.find_element(By.XPATH, '//div//p[text() = "There are no products to list in this category."]')
    assert cost_item.is_displayed(), 'El mensaje es incorrecto'

    continue_button : WebElement = driver.find_element(By.XPATH, '//div//a[text() = "Continue"]')
    assert continue_button.is_displayed(), 'El boton no se encuentra'
    continue_button.click()
    time.sleep (2)

    landing_page : WebElement = driver.find_element(By.XPATH, '//div[@id="slideshow0"]')
    assert landing_page.is_displayed(), 'No estas en Home Page'
    time.sleep(2)


def teardown():
    driver.quit()