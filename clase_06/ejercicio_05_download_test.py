import time
import pytest

import selenium_driver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver :WebDriver = None
def setup():
    global driver
    driver = selenium_driver.get_driver()
    url_pag ='https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html'

    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(url_pag)

def test_download():
    driver_wait= WebDriverWait(driver, 10)
    button_download : WebElement =driver.find_element((By.ID, "downloadButton"))
    assert button_download.is_displayed, 'No se encuentra el elemento  botón de descarga'
    button_download.click()
    driver_wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="progressbar"  and @aria-valuenow="100" ]')))
    driver_wait.until(EC.visibility_of_element_located(By.XPATH, '//div[@class="progress-label" and text()="Complete!" ]')) 
 
 

  
def teardown():
    driver.quit()
