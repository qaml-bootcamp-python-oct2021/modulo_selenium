
import factory_driver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import config_handler

driver :WebDriver = None
def setup():
    global driver
    driver = factory_driver.get_driver()

def _display():
    txt_display = 'Display'
    search_input: WebElement = driver.find_element(By.XPATH, '//div[@id="search"]//input')
    assert search_input.is_displayed, 'No se encuentra el elemento  barra de  busqueda'
    search_input.send_keys(txt_display)

    search_bar_button: WebElement = driver.find_element(By.XPATH, '//div[@id="search"]//button')
    assert search_bar_button.is_displayed, 'No se encuentra el elemento  botón de busqueda'
    search_bar_button.click()

    no_matches_txt: WebElement = driver.find_element(By.XPATH, '//p[contains(text(), "There is no product that matches the search")]')
    assert no_matches_txt.is_displayed, 'Se encontroaron resultdos en la busqueda'

    desciption_check: WebElement = driver.find_element(By.ID, 'description')
    assert desciption_check.is_displayed, 'No se encuentra el CHECK descripción'
    desciption_check.click()
   
   
    search_button: WebElement = driver.find_element(By.ID, 'button-search')
    assert search_button.is_displayed, 'No se encuentra el elemento  botón de busqueda'
    search_button.click()

    cinema_product_link :  get_link_by_text('Apple Cinema 30')
    ipod_nano_product_link :  get_link_by_text('iPod Nano')
    ipod_touche_product_link : get_link_by_text('iPod Touch')
    mac_product_link :  WebElement = get_link_by_text('MacBook Pro')
   
def get_link_by_text(text_link):
    link : WebElement = WebDriverWait(driver, config_handler.get_explicit_wait_small()).until(
         EC.presence_of_element_located((By.XPATH, f'//a[contains(text(), "{text_link}")]')))
    return link

def _mac():
    txt_desktops ='Desktops'
    menu_desktops: WebElement = driver.find_element(By.XPATH, f'//nav[@id="menu"]//a [contains(text(), "{txt_desktops}")]')
    assert menu_desktops.is_displayed, f'No se encuentra el menú {txt_desktops}'
    menu_desktops.click()

    name_submenu = "Mac"
    submenu: WebElement = driver.find_element(By.XPATH, f'//nav[@id="menu"]//a[contains(text(), "{name_submenu}")]')
    assert submenu.is_displayed, f'No se encuentra el submenú {name_submenu}'
    submenu.click()

    titulo_mac ='iMac'
    mac_img: WebElement =  WebDriverWait(driver, config_handler.get_explicit_wait_small()).until(
         EC.presence_of_element_located((By.XPATH, f'//img[@title="{titulo_mac}"]')))
    assert mac_img.is_displayed, f'No se encuentra la imagen con el tiulo {titulo_mac}'
    mac_img.click()
        
    car_btn: WebElement = driver.find_element(By.ID, 'button-cart')
    assert car_btn.is_displayed, 'Btn  agregar a carrito  no encontrado'
    car_btn.click()
   
    car_alert: WebElement =WebDriverWait(driver, config_handler.get_explicit_wait_small()).until(
         EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"alert-success") and contains (text(), "Success: You have added")]')))
    assert car_alert.is_displayed, 'Producto no agregado  a carrito de compras'

    car_total: WebElement = driver.find_element(By.XPATH, '//*[@id="cart-total"]')
    assert car_total.is_displayed, 'No existe carrito de compras'
    
    car_total_text = car_total.text.split("-")[1]

    image_price: WebElement = driver.find_element(By.XPATH, '//div[@id="content"]//ul[2]//h2')
    assert image_price.is_displayed, 'Precio  no identificado'
    assert car_total_text.strip() == image_price.text.strip() ,'Precio incorrecto'

def test_currency():
    dolar_currency = '$'
    currency_ico: WebElement = driver.find_element(By.XPATH, '//*[@id="form-currency"]//strong')
    assert dolar_currency == currency_ico.text, 'Moneda incorrecta'

    search_input: WebElement = driver.find_element(By.XPATH, '//div[@id="search"]//input')
    assert search_input.is_displayed, 'No se encuentra el elemento  barra de  busqueda'
    search_input.send_keys('Samsung')

def teardown():
    driver.quit()