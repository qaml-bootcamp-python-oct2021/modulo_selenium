from _typeshed import Self
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement
from selenium.common.exceptions import NoSuchElementException
import datetime

class BasePage:
    _driver : WebDriver

    def __init__(self, driver) -> None:
        self._driver = driver

    def close_browser(self):
        self._driver.quit()
    
    def take_screenshot(self, filename=f'{datetime.datetime.today().strftime("%Y%m%d_%H%M%S")}'):
        self._driver.save_screenshot(f'{filename}.png')

    def get_element (self, locator)-> WebElement:
        try:
            return self._driver.find_element(locator[0], locator[1])
        except NoSuchElementException:
            return None

    #Convirtiendo error en un valor bool
    def is_displayed (self, locator):
        element = self.get_element(locator)
        if element != None:
            return True
        return False