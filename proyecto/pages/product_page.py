from proyecto.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from proyecto.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage (BasePage):
    
    _laptop_netbook_bar = (By.XPATH,'//li//a[text() = "Laptops & Notebooks"]')
    _sub_menu_windows = (By.XPATH, '//li//a[text() = "Windows (0)"]')
    _mensaje_error_cat_vacia = (By.XPATH, '//div//p[text() = "There are no products to list in this category."]')

    def category_bar(self):
        self.verify_element_visible(self._laptop_netbook_bar), 'No se encontro el elemento'
        self.get_element(self._laptop_netbook_bar).click()
        
    def subcat_bar(self):    
        self.verify_element_visible(self._sub_menu_windows), 'No se encontrio el elemento'
        self.get_element(self._sub_menu_windows).click()

    def cat_vacia_error(self):
        self.verify_element_visible(self._mensaje_error_cat_vacia), 'El mensaje de error es incorrecto'
        self.get_element(self._mensaje_error_cat_vacia) 