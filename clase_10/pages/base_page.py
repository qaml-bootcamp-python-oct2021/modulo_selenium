
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
import datetime
class BasePage:
    _driver: WebDriver
    def __init__(self,driver) -> None:
        self._driver= driver

    def close_browser(self):
        self._driver.quit()
    
    def take_screenshot(self, filename=f'{datetime.datetime.today().strftime("%Y%m%d")}'):
        self._driver.save_screenshot(f'{filename}.png')
    
    def _get_element(self, locator)-> WebElement:
        assert self._exist_element(locator), 'El elemento no existe'
        return self._driver.find_element(locator[0], locator[1])
      

    def _exist_element(self,locator):
        try:
            return self._driver.find_element(locator[0], locator[1]) != None
        except NoSuchElementException:
            False

    def is_display(self, locator):
          assert self._get_element(locator).is_displayed(), 'No esta visible el elemento'