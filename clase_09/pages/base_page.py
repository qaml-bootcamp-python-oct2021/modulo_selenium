from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
import datetime

class BasePage:

    _driver : WebDriver

    def __init__ (self, driver) -> None:
        self._driver = driver

    def close_browser (self):
        self._driver.quit()

    def take_screenshot(self, filename =f'{ datetime.datetime.today().strftime("%Y%m%d")}'):
        self._driver.save_screenshot(f'{filename}.png')

    def _exist(self, locator):
        try: 
            return self._driver.find_element(locator[0], locator [1])
        except NoSuchElementException:
            return None

    def _get_element (self, locator):
        try: 
            return self._driver.find_element(locator[0], locator [1])
        except NoSuchElementException:
            return None

    