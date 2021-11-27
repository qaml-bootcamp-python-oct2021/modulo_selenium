from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest

driver : WebDriver = None
url = 'https://laboratorio.qaminds.com'

def get_driver():
    global driver
    driver_path = './driver/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)
    
def setup():
    get_driver()
    driver.maximize_window()
    driver.get(url)

@pytest.mark.ejemplo_explicit
def test_close_modal():
    text_expected = 'Laboratotio de entrenamiento y educación'
    driver_wait : WebDriverWait = WebDriverWait(driver,5) # 5 segundos para wait
    locator_modal = (By.XPATH, '//div[@role="dialog"]')
    modal : WebElement = driver_wait.until(ec.visibility_of_all_elements_located(locator_modal))
    assert modal.is_displayed() , 'No existe el modal'

    close_modal : WebElement = driver.find_element(By.XPATH, '//button[@data.testid="close-button"]')
    assert close_modal.is_displayed() , 'No existe el icono para cerrar el modal'
    close_modal.click()
    title : WebElement = driver.find_element(By.XPATH, f'//div[contains(@class, "active")]//span[text()= "{text_expected}]')
    assert title.is_displayed(), 'No se encuentra el titulo'
    assert text_expected.upper() == title.text , 'No coinciden los textos'


def teardown():
    driver.quit()
