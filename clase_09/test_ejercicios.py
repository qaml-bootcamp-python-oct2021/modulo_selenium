from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest
import factory_driver, config_handler

driver : WebDriver = None

def setup():
    global driver
    driver = factory_driver.get_driver()

@pytest.mark.test1
def test_busca_display():
    producto = 'Display'
    text_message ='There is no product that matches the search criteria.'
    barra_search : WebElement = driver.find_element(By.XPATH, '//div[@id="search"]//input')
    assert barra_search.is_displayed() , "No se encuentra la barra de busqueda"
    barra_search.send_keys(producto)
    boton_search : WebElement = driver.find_element(By.XPATH, '//div[@id="search"]//button')
    assert boton_search.is_displayed() , "No se encuentra el boton de busqueda"
    boton_search.click()
    message : WebElement = driver.find_element(By.XPATH, '//div[@id="content"]//p[text()="There is no product that matches the search criteria."]')
    assert message.is_displayed() and message.text == text_message, "No se encuentra le mensaje"
    check_button : WebElement = driver.find_element(By.ID,"description")
    assert check_button.is_displayed(), 'No se encuentra el boton'
    check_button.click()
    boton_search = driver.find_element(By.ID,"button-search")
    assert boton_search.is_displayed(), 'No se encuentra el boton de busqueda'
    boton_search.click()
    apple_product : WebElement = driver.find_element(By.XPATH, '//img[contains(@title,"Apple Cinema")]')
    assert apple_product.is_displayed() , 'No se encuentra el producto'
    ipod_product : WebElement = driver.find_element(By.XPATH, '//img[@title="iPod Nano"]')
    assert ipod_product.is_displayed() , 'No se encuentra el producto'
    ipod_touch_product : WebElement = driver.find_element(By.XPATH, '//img[@title="iPod Touch"]')
    assert ipod_touch_product.is_displayed() , 'No se encuentra el producto'
    mac_product : WebElement = driver.find_element(By.XPATH, '//img[@title="MacBook Pro"]')
    assert mac_product.is_displayed() , 'No se encuentra el producto'

@pytest.mark.test2
def test_verifica_carrito():
    cart_total_expected ="1 item(s) - $122.00"
    menu_desktops : WebElement = driver.find_element(By.XPATH, '//ul[@class="nav navbar-nav"]//a[text()="Desktops"]')
    assert menu_desktops.is_displayed() , "No se encuentra la opcion Desktops en el menu"
    menu_desktops.click()
    button_mac : WebElement = driver.find_element(By.XPATH,'//a[contains(text(),"Mac")]')
    assert button_mac.is_displayed() , "No se encuentra la opcion Windows"
    button_mac.click()
    imac_product : WebElement = driver.find_element(By.XPATH, '//img[@title="iMac"]')
    assert imac_product.is_displayed() , 'No se encuentra el producto'
    imac_product.click()
    add_to_cart : WebElement = driver.find_element(By.XPATH, '//button[@id="button-cart"]')
    assert add_to_cart.is_displayed(), 'No se encuentra el boton agregar al carrito'
    add_to_cart.click()
    cart_total : WebElement = driver.find_element(By.XPATH, '//span[@id="cart-total" and contains(text(),"1 item(s) - $122.00")]')
    assert cart_total_expected == cart_total.text , "No coinciden las cantidades"

@pytest.mark.test3
def test_currency():
    producto = 'Samsung'
    currency_logo : WebElement = driver.find_element(By.XPATH, '//button[@class="btn btn-link dropdown-toggle" and contains(text(),"$ Currency")]')
    print(currency_logo.text)
    assert currency_logo.is_displayed() and currency_logo.text == "$ Currency" , "No se encuentra le simbolo $ en currency"
    barra_search : WebElement = driver.find_element(By.XPATH, '//div[@id="search"]//input')
    assert barra_search.is_displayed() , "No se encuentra la barra de busqueda"
    barra_search.send_keys(producto)
    boton_search : WebElement = driver.find_element(By.XPATH, '//div[@id="search"]//button')
    assert boton_search.is_displayed() , "No se encuentra el boton de busqueda"
    boton_search.click()



def teardown():
    driver.quit()