import selenium_driver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

driver :WebDriver = None
url_pag ='https://demo.seleniumeasy.com/'

def setup():
    global driver
    browser = 'chrome'
    driver = selenium_driver.get_driver(browser)
    driver.get(url_pag)
    driver.maximize_window()


def test_close_modal():
    driver_w : WebDriverWait = WebDriverWait (driver,10)
    locator_modal = (By.XPATH, '//a[text() = "No, thanks!"]')
    modal : WebElement = driver_w.until(ec.visibility_of_element_located(locator_modal))
  
def teardown():
    driver.quit()