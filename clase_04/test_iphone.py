from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import selenium_driver
import time

driver : WebDriver = None

url = 'https://laboratorio.qaminds.com/'

def setup():
    global driver
    driver = selenium_driver.get_driver('chrome')
    driver.get(url)
    driver.maximize_window()

def test_iphone_search():
    producto = 'iPhone'

    input_search : WebElement = driver.find_element(By.XPATH,'//div[@id="search"]//input')
    assert input_search.is_displayed() , 'No se encuentra la barra de busqueda'
    input_search.send_keys(producto)
    button_search : WebElement = driver.find_element(By.XPATH,'//div[@id="search"]//button')
    assert button_search.is_displayed() , 'No se encuentra el boton de busqueda'
    button_search.click()
    imagen_iphone : WebElement = driver.find_element(By.XPATH,f'//img[@title="{producto}"]')
    assert imagen_iphone.is_displayed() ,'No se encontro imagen del producto'
    time.sleep(3)
    

def test_macbookpro_search():
    producto = 'MacBook Pro'

    input_search : WebElement = driver.find_element(By.XPATH,'//div[@id="search"]//input')
    assert input_search.is_displayed() , 'No se encuentra la barra de busqueda'
    input_search.send_keys(producto)
    button_search : WebElement = driver.find_element(By.XPATH,'//div[@id="search"]//button')
    assert button_search.is_displayed() , 'No se encuentra el boton de busqueda'
    button_search.click()
    imagen_iphone : WebElement = driver.find_element(By.XPATH,f'//img[@title="{producto}"]')
    assert imagen_iphone.is_displayed() ,'No se encontro imagen del producto'
    time.sleep(3)
    

def teardown():
    driver.quit()