from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import pytest

driver : WebDriver = None
#url = 'https://qamindslab.com/#/'
url = 'https://laboratorio.qaminds.com'

def get_driver():
    global driver
    driver_path = './driver/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)
    
def setup():
    get_driver()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(url)

@pytest.mark.ejemplo_implicit
def test_close_modal():
    text_expected = 'Laboratotio de entrenamiento y educación'
    modal : WebElement = driver.find_element(By.XPATH, '//div[@role="dialog"]')
    assert modal.is_displayed() , 'No existe el modal'
    close_modal : WebElement = driver.find_element(By.XPATH, '//button[@data.testid="close-button"]')
    assert close_modal.is_displayed() , 'No existe el icono para cerrar el modal'
    close_modal.click()
    title : WebElement = driver.find_element(By.XPATH, f'//div[contains(@class, "active")]//span[text()= "{text_expected}]')
    assert title.is_displayed(), 'No se encuentra el titulo'
    assert text_expected.upper() == title.text , 'No coinciden los textos'


@pytest.mark.actividad_iphone
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
    text_samsung : WebElement = driver.find_element(By.XPATH, f'//div[@class="caption"]//a[text()="Samnsung"]') #diseñado para fallar
    assert text_samsung.is_displayed() , "No se encontro el texto del Samnsung"

def teardown():
    driver.quit()
