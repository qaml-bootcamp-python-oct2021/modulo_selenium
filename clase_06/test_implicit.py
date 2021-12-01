from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import selenium_driver

driver : WebDriver = None

url = 'https://qamindslab.com/#/'

def setup():
    global driver
    driver = selenium_driver.get_driver('chrome')
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(url)

def test_close_modal():
    text_expected = 'Laboratorio de entrenamiento y educación'
    modal : WebElement = driver.find_element(By.XPATH,'//div[@role="dialog"]')
    assert modal.is_displayed() , 'No existe el modal'
    close_modal : WebElement = driver.find_element(By.XPATH,'//button[@data-testid="close-button"]')
    assert close_modal.is_displayed() , 'No existe el icono para cerrar el modal'
    close_modal.click()
    title : WebElement = driver.find_element(By.XPATH,f'//div[contains(@class,"active")]//span[text() = "{text_expected}"]')
    assert title.is_displayed(), 'No se encuentra el titulo'
    assert text_expected.upper() == title.text , 'No coinciden los texto'

def test_close_modal_negative():
    text_expected = 'Laboratorio de entrenamiento y educación'
    modal : WebElement = driver.find_element(By.XPATH,'//div[@role="modal"]')
    assert modal.is_displayed() , 'No existe el modal'
    close_modal : WebElement = driver.find_element(By.XPATH,'//button[@data-testid="close-button"]')
    assert close_modal.is_displayed() , 'No existe el icono para cerrar el modal'
    close_modal.click()
    title : WebElement = driver.find_element(By.XPATH,f'//div[contains(@class,"active")]//span[text() = "{text_expected}"]')
    assert title.is_displayed(), 'No se encuentra el titulo'
    assert text_expected.upper() == title.text , 'No coinciden los texto'

def teardown():
    driver.quit()