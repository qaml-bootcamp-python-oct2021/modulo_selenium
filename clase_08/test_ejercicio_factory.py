from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import pytest
import factory_driver

driver : WebDriver = None

def setup():
    global driver
    driver = factory_driver.get_driver()
    

@pytest.mark.ejercicio01
def test_busca_iphone():
    producto = 'iPhone'
    barra_search : WebElement = driver.find_element(By.XPATH, '//div[@id="search"]//input')
    assert barra_search.is_displayed() , "No se encuentra la barra de busqueda"
    barra_search.send_keys(producto)
    boton_search : WebElement = driver.find_element(By.XPATH, '//div[@id="search"]//button')
    assert boton_search.is_displayed() , "No se encuentra el boton de busqueda"
    boton_search.click()
    imagen_iphone : WebElement = driver.find_element(By.XPATH, f'//img[@title="{producto}"]')
    assert imagen_iphone.is_displayed() , "No se encontro la imagen del producto"

@pytest.mark.ejercicio02
def test_tablets():
    menu_tablets : WebElement = driver.find_element(By.XPATH, '//ul[@class="nav navbar-nav"]//a[text()="Tablets"]')
    assert menu_tablets.is_displayed() , "No se encuentra la opcion Tablets en el menu"
    menu_tablets.click()
    producto_samsung : WebElement = driver.find_element(By.XPATH, '//div[@class="caption"]//a[text()="Samsung Galaxy Tab 10.1"]' )
    assert producto_samsung.is_displayed() , "No se encuentra el producto"
    producto_samsung.click()
    producto_precio : WebElement = driver.find_element(By.XPATH, '//li[contains(h2,"$241.99")]')
    assert producto_precio.is_displayed() , "No se muestra el precio del producto"
    add_wish_list : WebElement = driver.find_element(By.XPATH, '//button[@data-original-title="Add to Wish List"]')
    assert add_wish_list.is_enabled() , "No se puede agregar a la Wish List"
    add_wish_list.click()
    add_to_cart : WebElement = driver.find_element(By.XPATH, '//button[@id="button-cart"]')
    add_to_cart.click()
    cart_total : WebElement = driver.find_element(By.XPATH,'//span[@id="cart-total"]')
    assert cart_total.text == "0 item(s) - $0.00" , "No se agregaron elementos al carrito"

@pytest.mark.ejercicio03
def test_back_home():
    message = "There are no products to list in this category."
    menu_laptops : WebElement = driver.find_element(By.XPATH, '//ul[@class="nav navbar-nav"]//a[text()="Laptops & Notebooks"]')
    assert menu_laptops.is_displayed() , "No se encuentra la opcion Laptos & Notebooks en el menu"
    menu_laptops.click()
    button_windows : WebElement = driver.find_element(By.XPATH,'//a[contains(text(),"Windows")]')
    assert button_windows.is_displayed() , "No se encuentra la opcion Windows"
    button_windows.click()
    container_message : WebElement = driver.find_element(By.XPATH,'//div[@id="content"]//p')
    assert container_message.is_displayed() and container_message.text == message , "No se encuentra ningun mensaje"
    button_continue : WebElement = driver.find_element(By.XPATH, '//a[text()="Continue"]')
    assert button_continue.is_displayed() , "No se encuentra el boton Continue"
    button_continue.click()
    home : WebElement = driver.find_element(By.XPATH, '//div[@id="common-home"]')
    assert home.is_displayed() , "No estas en la pagina de Inicio"

def teardown():
    driver.quit()