from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import factory_driver

driver : WebDriver = None


def setup():
    global driver
    driver = factory_driver.get_driver()
    

def test_start_download():  
    driver_w : WebDriverWait = WebDriverWait(driver,5)
    button_download : WebElement = driver.find_element(By.ID,'downloadButton')
    assert button_download.is_displayed() , 'No se encuentra el boton Start Download'
    button_download = driver_w.until(ec.element_to_be_clickable(button_download))
    button_download.click()
    title_download : WebElement = driver.find_element(By.ID,'ui-id-1')
    button_cancel : WebElement = driver.find_element(By.XPATH,'//button[text() = "Cancel Download"]')
    assert title_download.is_displayed() , 'No se encuentra el titulo File Download'
    assert button_cancel.is_displayed() , 'No se encuentra el boton Cancel Download'
    completed_message = (By.XPATH,'//div[@id="dialog"]/div[text()="Complete!"]')
    verify_element_visible(completed_message,10,'Complete Message')
    close_button_locator = (By.XPATH,'//button[text() = "Close"]')
    button_close : WebElement = verify_element_visible(close_button_locator,10,'Boton Close')
    button_close.click()

def verify_element_visible(locator,timeout,locator_message):
    driver_w : WebDriverWait = WebDriverWait(driver,timeout)
    try:
        element = driver_w.until(ec.visibility_of_element_located(locator))
        return element
    except TimeoutException as e:
        assert False , f'No fue posible encontrar el elemento {locator_message} en {timeout} segundos'


def teardown():
    driver.quit()