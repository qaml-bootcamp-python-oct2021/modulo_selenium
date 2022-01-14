from proyecto_final.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SearchPage(BasePage):

    _search_criteria_title = (By.XPATH,'//h2[text()="Products meeting the search criteria"]')
    _input_search = (By.ID, 'input-search')
    _select_category = (By.XPATH,'//select[@name="category_id"]')
    

    def __init__(self,driver) -> None:
        super().__init__(driver)
    
    def _get_product_image(self,product):
        locator = f'//div[@class="image"]//img[@title="{product}"]'
        product_image = (By.XPATH, locator)
        return product_image
    
    def verify_product_image(self,product):
        assert self.is_displayed(self._get_product_image(product)), f'No se encuentra la imagen del producto {product} en la pagina'

    def verify_search_criteria_title(self):
        assert self.is_displayed(self._search_criteria_title), 'No se encuentra el titulo Products meeting the search criteria en la pagina'
    
    def verify_input_search(self):
        assert self.is_displayed(self._input_search), 'No se encuentra la barra de busqueda en la pagina'
    
    def verify_select_category(self):
        assert self.is_displayed(self._select_category), 'No se encuentra el selector de categoria en la pagina'
    
    def verify_search_page(self):
        self.verify_search_criteria_title()
        self.verify_input_search()
        self.verify_select_category()
    
    def click_on_product(self,product):
        self.verify_product_image(product)
        self.get_element(self._get_product_image(product)).click()