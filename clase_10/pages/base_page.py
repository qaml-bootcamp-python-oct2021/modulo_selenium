
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import datetime
class BasePage:
    _driver: WebDriver
    def __init__(self,driver) -> None:
        self._driver= driver

    def close_browser(self):
        self._driver.quit()
    
    def take_screenshot(self, filename=f'{datetime.datetime.today().strftime("%Y%m%d")}'):
        self._driver.save_screenshot(f'{filename}.png')
    
    def get_element(self, locator)-> WebElement:
        try:
            return self._driver.find_element(locator[0], locator[1]) 
        except NoSuchElementException:
            return None
    

    def is_displayed(self, locator):
         return  self.get_element(locator) != None

    def verify_element_visible(self, locator,timeout, description):
        wait_driver= WebDriverWait(self._driver, timeout)
        isVisible = False
        try:
            wait_driver.until(ec.visibility_of_element_located(locator))
            isVisible = True
        except TimeoutException:
            self.take_screenshot()
        assert isVisible, f'No fue posible identificar a {description} en {timeout} segundos'

