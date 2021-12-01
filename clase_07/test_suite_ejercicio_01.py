import time
import pytest
import factory_driver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

driver :WebDriver = None
def setup():
    global driver
    driver = factory_driver.get_driver(factory_driver.FIREFOX)
    url_pag ='https://laboratorio.qaminds.com/'
    driver.get(url_pag)
    driver.maximize_window()
  

def test_search_iphone():
    search_input: WebElement = driver.find_element(By.XPATH, '//div[@id="search"]//input')
    assert search_input.is_displayed, 'No se encuentra el elemento  barra de  busqueda'
    search_input.send_keys('Iphone')

    search_button: WebElement = driver.find_element(By.XPATH, '//div[@id="search"]//button')
    assert search_button.is_displayed, 'No se encuentra el elemento  botón de busqueda'
    search_button.click()
    
    image_finded: WebElement = driver.find_element(By.XPATH, '//img[@title="iPhone"]')
    assert image_finded.is_displayed, 'No se encontro imagen de producto'
    image_finded.click()

def test_menu_tablet():
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

def test_menu_window():
       
    name_menu = "Laptops & Notebooks"
    menu: WebElement = driver.find_element(By.XPATH, f'//nav[@id="menu"]//a[contains(text(), "{name_menu}")]')
    assert menu.is_displayed, f'No se encuentra el menú {name_menu}'
    menu.click()
    name_submenu = "Windows"
    submenu: WebElement = driver.find_element(By.XPATH, f'//nav[@id="menu"]//a[contains(text(), "{name_submenu}")]')
    assert submenu.is_displayed, f'No se encuentra el submenú {name_submenu}'
    submenu.click()

   

def teardown():
    driver.quit()