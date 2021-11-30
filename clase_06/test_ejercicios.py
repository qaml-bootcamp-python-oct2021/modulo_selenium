from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest

driver : WebDriver = None
#url = 'https://demo.seleniumeasy.com'
#url ='https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html'

def get_driver():
    global driver
    driver_path = './driver/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)
    
def setup():
    get_driver()
    driver.maximize_window()
    #driver.get(url)

@pytest.mark.ejercicio_explicit
def test_close_modal():
    driver.get('https://demo.seleniumeasy.com')
    driver_wait : WebDriverWait = WebDriverWait(driver,5) # 5 segundos para wait
    locator_modal = (By.ID, 'at-cv-lightbox-win')
    driver_wait.until(ec.visibility_of_all_elements_located(locator_modal))
    close_modal : WebElement = driver.find_element(By.XPATH, '//a[@id="at-cv-lightbox-close"]')
    assert close_modal.is_displayed() , 'No existe el icono para cerrar el modal'
    close_modal.click()

@pytest.mark.ejercicio_download1
def test_download1():
    driver.get('https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html')
    driver_wait : WebDriverWait = WebDriverWait(driver,5)
    button_download : WebElement = driver.find_element(By.ID,'downloadButton')
    assert button_download.is_displayed(),'No se encuentra el boton download'
    button_download = driver_wait.until(ec.element_to_be_clickable(button_download))
    button_download.click()
    driver_wait : WebDriverWait = WebDriverWait(driver,10)
    locator_complete= (By.XPATH, '//div[@id="dialog"]/div[text()="Complete!"]')
    driver_wait.until(ec.visibility_of_element_located(locator_complete))
    locator_close_button = (By.XPATH,'//button[text()="Close"]')
    button_close : WebElement = driver_wait.until(ec.visibility_of_element_located(locator_close_button))
    button_close.click()

@pytest.mark.ejercicio_download2
def test_download2():
    driver.get('https://demo.seleniumeasy.com/bootstrap-download-progress-demo.html')
    driver_wait : WebDriverWait = WebDriverWait(driver,25)
    button_download_locator = (By.ID,'cricle-btn')
    button_download : WebElement = driver_wait.until(ec.visibility_of_element_located(button_download_locator))
    button_download.click()
    text_percent_locator = (By.XPATH, '//div[@class="percenttext"]')
    driver_wait.until(ec.text_to_be_present_in_element(text_percent_locator, "100%"))

@pytest.mark.ejercicio_alertmessage
def test_alert_message():
    message_text ="I'm an autocloseable success message. I will hide in 5 seconds"
    driver.get('https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html')
    driver_wait : WebDriverWait = WebDriverWait(driver,10)
    button_alert_locator = (By.ID,'autoclosable-btn-success')
    button_alert : WebElement = driver_wait.until(ec.visibility_of_element_located(button_alert_locator))
    button_alert.click()
    message_locator = (By.XPATH, '//div[contains(@class,"alert-autocloseable-success")]')
    driver_wait.until(ec.text_to_be_present_in_element(message_locator, message_text))
    driver_wait.until(ec.invisibility_of_element_located(message_locator))

def teardown():
    driver.quit()
