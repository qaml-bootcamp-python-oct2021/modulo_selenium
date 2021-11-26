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

# def test_iphone_search():
#     producto = 'iPhone'

#     input_search : WebElement = driver.find_element(By.XPATH,'//div[@id="search"]//input')
#     assert input_search.is_displayed() , 'No se encuentra la barra de busqueda'
#     input_search.send_keys(producto)
#     button_search : WebElement = driver.find_element(By.XPATH,'//div[@id="search"]//button')
#     assert button_search.is_displayed() , 'No se encuentra el boton de busqueda'
#     button_search.click()
#     imagen_iphone : WebElement = driver.find_element(By.XPATH,f'//img[@title="{producto}"]')
#     assert imagen_iphone.is_displayed() ,'No se encontro imagen del producto'
#     time.sleep(3)
    

# def test_macbookpro_search():
#     producto = 'MacBook Pro'

#     input_search : WebElement = driver.find_element(By.XPATH,'//div[@id="search"]//input')
#     assert input_search.is_displayed() , 'No se encuentra la barra de busqueda'
#     input_search.send_keys(producto)
#     button_search : WebElement = driver.find_element(By.XPATH,'//div[@id="search"]//button')
#     assert button_search.is_displayed() , 'No se encuentra el boton de busqueda'
#     button_search.click()
#     imagen_iphone : WebElement = driver.find_element(By.XPATH,f'//img[@title="{producto}"]')
#     assert imagen_iphone.is_displayed() ,'No se encontro imagen del producto'
#     time.sleep(3)

def test_login_error():
    #Configuracion
    login_url = 'https://laboratorio.qaminds.com/index.php?route=account/login'
    usuario = 'usuario'
    password = '1234'
    error_message = 'Warning: No match for E-Mail Address and/or Password.'
    driver.get(login_url)
    form_content : WebElement = driver.find_element(By.ID,'content')
    assert form_content.is_displayed(), 'No estan visibles los formularios de Registro y Login'

    # Acciones
    input_email : WebElement = driver.find_element(By.ID,'input-email')
    assert input_email.is_displayed() , 'No se encuentra el input de email en formulario'
    input_email.send_keys(usuario) 
    input_pass : WebElement = driver.find_element(By.ID,'input-password')
    assert input_pass.is_displayed() , 'No se encuentra el input de password en formulario'
    input_pass.send_keys(password)
    button_login : WebElement = driver.find_element(By.XPATH,'//input[@type="submit"]')
    assert button_login.is_displayed() , 'No se encuentra el boton de login en formulario'
    button_login.click()
    #aserciones
    mensaje : WebElement = driver.find_element(By.XPATH, f'//div[text()=" {error_message}"]')
    assert error_message == mensaje.text , 'No coinciden los mensajes'

def teardown():
    driver.quit()