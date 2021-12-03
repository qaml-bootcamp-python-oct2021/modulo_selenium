from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import factory_driver

driver : WebDriver = None
short = 5
medium = 10
large = 20


def setup():
    global driver
    driver = factory_driver.get_driver()


def test_close_modal():
    text_expected = 'Laboratorio de entrenamiento y educación'
    driver_w : WebDriverWait = WebDriverWait(driver,short)
    locator_modal = (By.XPATH,'//div[@role="dialogo"]')
    modal : WebElement = driver_w.until(ec.visibility_of_element_located(locator_modal))
    assert modal.is_displayed() , 'No existe el modal'
    close_modal : WebElement = driver.find_element(By.XPATH,'//button[@data-testid="close-button"]')
    assert close_modal.is_displayed() , 'No existe el icono para cerrar el modal'
    close_modal.click()
    title : WebElement = driver.find_element(By.XPATH,f'//div[contains(@class,"active")]//span[text() = "{text_expected}"]')
    assert title.is_displayed(), 'No se encuentra el titulo'
    assert text_expected.upper() == title.text , 'No coinciden los texto'

def teardown():
    driver.quit()