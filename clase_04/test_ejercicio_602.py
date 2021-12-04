from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import selenium_driver
import pytest

driver : WebDriver = None

url = 'https://demo.seleniumeasy.com/'

def setup():
    global driver
    browser = 'chrome'
    driver = selenium_driver.get_driver(browser)
    #driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(url)

@pytest.mark.qaminds
def test_close_banner():
    #closing welcome banner, using explicit wait
    driver_w : WebDriverWait =  WebDriverWait(driver, 15)
    loc_tup_close_btn = (By.ID,"at-cv-lightbox-close")
    banner_close_button = driver_w.until(ec.element_to_be_clickable(loc_tup_close_btn))
    #assert banner_close_button.is_displayed(), 'No se encuentra el boton para cerrar'
    banner_close_button.click()

def teardown():
    driver.quit()