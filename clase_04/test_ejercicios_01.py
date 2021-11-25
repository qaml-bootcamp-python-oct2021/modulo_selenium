from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time
import pytest

driver : WebDriver = None
url = 'https://laboratorio.qaminds.com'

def get_driver():
    global driver
    driver_path = './driver/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)
    
def setup():
    get_driver()
    driver.get(url)
    driver.maximize_window()

@pytest.mark.ejercicio01
def test_busca_iphone():
    producto = 'iPhone'
    barra_search : WebElement = driver.find_element(By.XPATH, '//div[@id="search"]//input')
    assert barra_search.is_displayed() , "No se encuentra la barra de busqueda"
    barra_search.send_keys(producto)
    boton_search : WebElement = driver.find_element(By.XPATH, '//div[@id="search"]//button')
    assert boton_search.is_displayed() , "No se encuentra el boton de busqueda"
    boton_search.click()
    time.sleep(1)
    imagen_iphone : WebElement = driver.find_element(By.XPATH, f'//img[@title="{producto}"]')
    assert imagen_iphone.is_displayed() , "No se encontro la imagen del producto"
    time.sleep(2)

@pytest.mark.ejercicio02
def test_tablets():
    menu_tablets : WebElement = driver.find_element(By.XPATH, '//ul[@class="nav navbar-nav"]//a[text()="Tablets"]')
    assert menu_tablets.is_displayed() , "No se encuentra la opcion Tablets en el menu"
    menu_tablets.click()
    time.sleep(1)
    producto_samsung : WebElement = driver.find_element(By.XPATH, '//div[@class="caption"]//a[text()="Samsung Galaxy Tab 10.1"]' )
    assert producto_samsung.is_displayed() , "No se encuentra el producto"
    producto_samsung.click()
    time.sleep(1)
    producto_precio : WebElement = driver.find_element(By.XPATH, '//li[contains(h2,"$241.99")]')
    assert producto_precio.is_displayed() , "No se muestra el precio del producto"
    add_wish_list : WebElement = driver.find_element(By.XPATH, '//button[@data-original-title="Add to Wish List"]')
    assert add_wish_list.is_enabled() , "No se puede agregar a la Wish List"
    add_wish_list.click()
    time.sleep(1)
    add_to_cart : WebElement = driver.find_element(By.XPATH, '//button[@id="button-cart"]')
    add_to_cart.click()
    time.sleep(1)
    cart_total : WebElement = driver.find_element(By.XPATH,'//span[@id="cart-total"]')
    assert cart_total.text != "0 item(s) - $0.00" , "No se agregaron elementos al carrito"
    time.sleep(2)

@pytest.mark.ejercicio03
def test_invalid_login():
    fake_email = "juan@mail.com"
    fake_password = "test123"
    alert ="Warning: No match for E-Mail Address and/or Password."
    my_account : WebElement = driver.find_element(By.XPATH, '//div[@id="top-links"]//a[@title="My Account"]')
    assert my_account.is_displayed() , "No se encuentra el boton My Account"
    my_account.click()
    time.sleep(1)
    login : WebElement = driver.find_element(By.XPATH, '//ul[contains(@class,"dropdown-menu")]//a[text()="Login"]')
    assert login.is_displayed(), "No se encuentra el boton Login"
    login.click()
    time.sleep(1)
    input_email : WebElement = driver.find_element(By.XPATH, '//input[@id="input-email"]')
    input_email.is_enabled(), "No se puede escribir en el campo Email"
    input_email.send_keys(fake_email)
    input_password : WebElement =  driver.find_element(By.XPATH, '//input[@id="input-password"]')
    input_password.is_enabled(), "No se puede escribir en el campo Password"
    input_password.send_keys(fake_password)
    button_submit : WebElement = driver.find_element(By.XPATH,'//input[@type="submit"]')
    button_submit.click()
    time.sleep(1)
    alert_message : WebElement = driver.find_element(By.XPATH, '//div[contains(@class,"alert")]')
    assert alert_message.is_displayed() and alert_message.text == alert , "Credenciales Validas"
    time.sleep(3)

@pytest.mark.ejercicio04
def test_back_home():
    message = "There are no products to list in this category."
    menu_laptops : WebElement = driver.find_element(By.XPATH, '//ul[@class="nav navbar-nav"]//a[text()="Laptops & Notebooks"]')
    assert menu_laptops.is_displayed() , "No se encuentra la opcion Laptos & Notebooks en el menu"
    menu_laptops.click()
    time.sleep(1)
    button_windows : WebElement = driver.find_element(By.XPATH,'//a[contains(text(),"Windows")]')
    assert button_windows.is_displayed() , "No se encuentra la opcion Windows"
    button_windows.click()
    time.sleep(1)
    container_message : WebElement = driver.find_element(By.XPATH,'//div[@id="content"]//p')
    assert container_message.is_displayed() and container_message.text == message , "No se encuentra ningun mensaje"
    button_continue : WebElement = driver.find_element(By.XPATH, '//a[text()="Continue"]')
    assert button_continue.is_displayed() , "No se encuentra el boton Continue"
    button_continue.click()
    time.sleep(1)
    home : WebElement = driver.find_element(By.XPATH, '//div[@id="common-home"]')
    assert home.is_displayed() , "No estas en la pagina de Inicio"
    time.sleep(3)


def teardown():
    driver.quit()