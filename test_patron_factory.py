from typing import ItemsView
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import selenium_driver
import time
import factory_driver as f_driver

driver = WebDriver = None

def setup():
    global driver
    driver = f_driver.get_driver('firefox')
    driver.get('https://laboratorio.qaminds.com/')

def test_iphone():
    search_bar : WebElement = driver.find_element(By.XPATH, '//div[@id="search"]//input')
    assert search_bar.is_displayed() , 'No se encuentra la barra de busqueda'
    search_bar.send_keys('iPhone')
    search_button : WebElement = driver.find_element(By.XPATH, '//div[@id="search"]//button')
    assert search_button.is_displayed() , 'No se encuentra el boton de busqueda'
    search_button.click()
    image_iphone : WebElement = driver.find_element(By.XPATH, '//img[@title="iPhone"]')
    assert image_iphone.is_displayed() , 'No se encuentra la imagen'
    image_iphone.click()
    time.sleep(2)

def test_windows():
   
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

def test_tablet():
  
    tablet_element : WebElement = driver.find_element(By.XPATH, '//ul//a[text() = "Tablets"]')
    assert tablet_element.is_displayed(),'No se encuentra el elemento'
    tablet_element.click()
    time.sleep(2)

    tablet_img : WebElement = driver.find_element(By.XPATH, '//img[@title="Samsung Galaxy Tab 10.1"]')
    assert tablet_img.is_displayed(), 'No se encuentra la imagen'
    tablet_img.click()
    time.sleep(2)

    cost_item : WebElement = driver.find_element(By.XPATH, '//ul//h2[text() = "$241.99"]')
    assert cost_item.is_displayed(), 'El valor es incorrecto'

    wish_item : WebElement = driver.find_element(By.XPATH, '//div//button[@data-original-title="Add to Wish List"]')
    assert wish_item.is_displayed(), 'No se puede agregar a la wishlist'
    wish_item.click()

    add_item_cart : WebElement = driver.find_element(By.XPATH, '//div//button[@id="button-cart"]')
    assert add_item_cart.is_displayed(), 'No se puede agregar el producto al carrito'
    add_item_cart.click()

    time.sleep(2)


def teardown():
    driver.quit()