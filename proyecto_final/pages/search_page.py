from proyecto_final.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time
import logging
class SearchPage(BasePage):
    __path_div_content = '//div[@id="content"]'
    _locator_text_no_result = ( By.XPATH, f'{__path_div_content}/p[contains(text(), "There is no product")]')
    _locator_div_product = (By.XPATH, f'{__path_div_content}//div[contains(@class,"product-layout")]')
    
    def _get_locator_product_found(self, product_name):
        return (By.XPATH,f'//img[@title="{product_name}"]')


    def _verify_product_found(self, locator):
        assert self.is_displayed(locator) , 'No se encontró el producto buscado'

    def go_detail_product_found(self,product_name):
        locator_product = self._get_locator_product_found(product_name)
        self._verify_product_found(locator_product)
        self.get_element(locator_product).click()
