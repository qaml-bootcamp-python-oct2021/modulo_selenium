
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from proyecto_final.util import config_init
from proyecto_final.util import utils
import proyecto_final.util.constants as constants

import datetime
class BasePage:
    _driver: WebDriver
    def __init__(self,driver) -> None:
        self._driver= driver

    def _get_title_page(self):
        return self._driver.title

    def close_browser(self):
        self._driver.quit()
    
    def take_screenshot(self, module='gral',filename= datetime.datetime.today().strftime("%Y%m%d%H%M%S")):
        path_evidence= f'{config_init.get_config().get_evidence_path()}/{module}'
        utils.create_dir_files(path_evidence)
        self._driver.save_screenshot(f'{path_evidence}/{filename.strip()}.png')
    
    def get_element(self, locator)-> WebElement:
        try:
            return self._driver.find_element(locator[0], locator[1]) 
        except NoSuchElementException:
            self.take_screenshot(constants.EVIDENCE_ERROR,'get_element')
            return None

    def get_elements(self, locator)-> WebElement:
        try:
            return self._driver.find_elements(locator[0], locator[1]) 
        except NoSuchElementException:
            self.take_screenshot(constants.EVIDENCE_ERROR,'get_elements')
            return None
    

    def is_displayed(self, locator):
         return  self.get_element(locator) != None

    def verify_title_page(self, title_expected, module='gral'):
        try:
            assert title_expected == self._get_title_page()
        except AssertionError:
            self.take_screenshot(constants.EVIDENCE_ERROR, f'{module}_{title_expected}')
            raise AssertionError(f'Pág. actual:{ self._get_title_page()}, pág. esperada: {title_expected}.')

    def verify_element_visible(self, locator,timeout= 5, description = 'gral'):
        wait_driver= WebDriverWait(self._driver, timeout)
        isVisible = False
        try:
            wait_driver.until(ec.visibility_of_element_located(locator))
            isVisible = True
        except TimeoutException:
            self.take_screenshot(constants.EVIDENCE_ERROR,'verify_element_visible')
        assert isVisible, f'No fue posible identificar a {description} en {timeout} segundos'

    def verify_element_clickable(self,locator,timeout,descripcion):
        wait_driver= WebDriverWait(self._driver, timeout)
        result = False
        try:
            wait_driver.until(ec.element_to_be_clickable(locator))
            result = True
        except TimeoutException:
            self.take_screenshot(constants.EVIDENCE_ERROR,'verify_element_clickable')
        assert result , f'El elemento {descripcion} no es clickable.'
    
    def click_element(self, locator, timeout=5, name_element='element'):
        self.verify_element_clickable(locator,timeout, name_element)
        self.get_element(locator).click()
    
    def write_text_element(self, locator,text, timeout=5, name_element='element'):
        self.verify_element_visible(locator,timeout, name_element)
        self.get_element(locator).send_keys(text)
    

    
