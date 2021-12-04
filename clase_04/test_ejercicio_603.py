from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import selenium_driver
import pytest

driver : WebDriver = None

url = 'https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html'

def setup():
    global driver
    browser = 'chrome'
    driver = selenium_driver.get_driver(browser)
    #driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(url)

@pytest.mark.qaminds
def test_close_banner():
    #validating message "Complete" and Close button are displayed after download is done
    driver_w : WebDriverWait =  WebDriverWait(driver, 10)
    driver_dynamic: WebDriverWait = WebDriverWait(driver, 20)
    loc_tup_download_btn = (By.ID,"downloadButton")
    loc_tup_label = (By.XPATH,'//div[@class="progress-label"]')
    loc_tup_close_btn = (By.XPATH,'//button[@type="button"]')
    download_button = driver_w.until(ec.element_to_be_clickable(loc_tup_download_btn))
    download_button.click()
    complete_label = driver_dynamic.until(ec.text_to_be_present_in_element(loc_tup_label,"Complete!"))
    close_button = driver_dynamic.until(ec.text_to_be_present_in_element(loc_tup_close_btn,"Close"))
    close_button.click()

def teardown():
    driver.quit()