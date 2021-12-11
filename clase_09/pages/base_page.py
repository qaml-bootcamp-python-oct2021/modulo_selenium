from selenium.common import exceptions
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from clase_09.drivers import wait_driver
from selenium.webdriver.support import expected_conditions as ec
import datetime

class BasePage:

    _driver : WebDriver

    def __init__(self,driver) -> None:
        self._driver = driver

    def close_browser(self):
        self._driver.quit()

    def take_screenshot(self,filename=f'{datetime.datetime.today().strftime("%Y%m%d_%H%M%S")}'):
        self._driver.save_screenshot(f'{filename}.png')

    def get_element(self,locator) -> WebElement:
        try:
            return self._driver.find_element(locator[0],locator[1])
        except NoSuchElementException:
            return None

    def is_displayed(self,locator):
        element = self.get_element(locator)
        if element != None:
            return True
        return False

    def verify_element_visible(self,locator,timeout=0):
        w_driver = wait_driver.get_driver(self._driver,timeout)
        result = False
        try:
            w_driver.until(ec.visibility_of_element_located(locator))
            result = True
        except TimeoutException:
            pass
        try:
            assert result 
        except AssertionError:
            self.take_screenshot('AssertionError')
            raise AssertionError(f'No es posible encontrar el elemento {locator} en {timeout} segundos.')

    def verify_element_clickable(self,locator,timeout,descripcion):
        w_driver = wait_driver.get_driver(self._driver,timeout)
        result = False
        try:
            w_driver.until(ec.element_to_be_clickable(locator))
            result = True
        except TimeoutException:
            pass
        assert result , f'El elemento {descripcion} no es clickable.'