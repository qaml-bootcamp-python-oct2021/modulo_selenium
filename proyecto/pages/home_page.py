from selenium.webdriver.remote import webdriver
from proyecto.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    _logo = (By.XPATH,'//div[@id="logo"]//img')
    _new_image = (By.ID, 'image')
    _input_search = (By.XPATH,'//div[@id="search"]//input')
    _button_search = (By.XPATH,'//div[@id="search"]//button')
    
    def __init__(self, driver) -> None:
        super().__init__(driver)
    
    def verify_logo(self):
        assert self.is_displayed(self._logo) , 'No se encontro el Logo'

    def click_logo(self):
        self.verify_element_visible(self._logo, 3)
        self.get_element(self._logo).click()
    
    def verify_input_search(self):
        assert self.is_displayed(self._input_search) , 'No se encuentra el input de busqueda'

    def verify_button_search(self):
        assert self.is_displayed(self._button_search) , 'No se encuentra el boton de busqueda'
    
    def buscar_producto (self, producto):
        self.verify_input_search()
        self.get_element(self._input_search).send_keys(producto)
        self.verify_button_search()
        self.get_element(self._button_search).click()

    
    