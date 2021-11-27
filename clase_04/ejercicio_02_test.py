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

def test_menu_tablet():
    global driver
    url_pag ='https://laboratorio.qaminds.com/'
    driver.get(url_pag)
    current_url= driver.current_url
    assert url_pag == current_url, f'Url no coinciden,  actual:{current_url} buscada:{url_pag}'

    menu_a: WebElement = driver.find_element(By.XPATH, '//nav[@id="menu"]//a [contains(text(), "Tablets")]')
    assert menu_a.is_displayed, 'No se encuentra el menú Tablets'
    menu_a.click()

    tablet_img: WebElement = driver.find_element(By.XPATH, '//img[@title="Samsung Galaxy Tab 10.1"]')
    assert tablet_img.is_displayed, 'No se encuentra la imagen'
    tablet_img.click()
    
    image_price: WebElement = driver.find_element(By.XPATH, '//div[@id="content"]//ul[2]//h2')
    assert image_price.is_displayed, 'Precio  no identificado'
    assert image_price.text == '$241.99','Precio incorrecto'

    wish_btn: WebElement = driver.find_element(By.XPATH, '//button[@data-original-title="Add to Wish List"]')
    assert wish_btn.is_displayed, 'Btn  agregar a lista  no encontrado'
    wish_btn.click()
    time.sleep(3)
    wish_alert: WebElement = driver.find_element(By.CLASS_NAME, 'breadcrumb')
    assert wish_alert.is_displayed ,'Producto  no  agregado a lista de deseos'
    car_btn: WebElement = driver.find_element(By.ID, 'button-cart')
    assert car_btn.is_displayed, 'Btn  agregar a carrito  no encontrado'
    car_btn.click()
    time.sleep(3)
    car_total: WebElement = driver.find_element(By.XPATH, '//div[contains(@class,"alert-success") and contains (text(), "Success: You have added")]')
    assert car_total.is_displayed, 'Producto no agregado  a carrito de compras'


    
    

def teardown():
    driver.quit()