from clase_10.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    _logo = (By.XPATH,'//div[@id="logo"]//img')
    _button_search = (By.XPATH,'//div[@id="search"]//button')
    _input_search = (By.XPATH,'//div[@id="search"]//input')

    
    def __init__(self, driver) -> None:
         super().__init__(driver)
    
    def verify_logo(self):
        assert self.is_displayed( self._logo), 'Logo no encontrado' 

    def click_logo(self):
        self.verify_element_visible( self._logo, 5, 'Logo')
        self.get_element(self._logo).click()


    def verify_input_search(self):
        assert self.is_displayed(self._input_search) , 'No se encuentra el input de búsqueda'

    def verify_button_search(self):
        assert self.is_displayed(self._button_search) , 'No se encuentra el botón de búsqueda'

    def search_producto(self,product_name):
        self.verify_input_search()
        self.get_element(self._input_search).send_keys(product_name)
        self.verify_button_search()
        self.get_element(self._button_search).click()
 