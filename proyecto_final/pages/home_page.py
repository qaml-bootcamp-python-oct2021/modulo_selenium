from proyecto_final.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    _logo = (By.ID, "logo")
    _input_search = (By.XPATH, '//input[@name="search"]')
    _button_search = (By.XPATH, '//div[@id="search"]//button')
    _slideshow = (By.ID, "slideshow0")
    _carousel = (By.ID, "carousel0")
    
    def __init__(self, driver) -> None:
         super().__init__(driver)

    def verify_slideshow(self):
        assert self.is_displayed(self._slideshow), 'No se encuentra el Slideshow en la pagina'

    def verify_carousel(self):
        assert self.is_displayed(self._carousel), 'No se encuentra el Carrusel en la pagina '

    def verify_logo(self):
        assert self.is_displayed(self._logo) , 'No se encontro el Logo'

    def verify_home_page(self):
        self.verify_logo()
        self.verify_slideshow()
        self.verify_carousel()

    def click_logo(self):
        self.verify_element_visible(self._logo,5)
        self.get_element(self._logo).click()

    def verify_input_search(self):
        assert self.is_displayed(self._input_search) , 'No se encuentra el input de busqueda'

    def verify_button_search(self):
        assert self.is_displayed(self._button_search) , 'No se encuentra el boton de busqueda'

    def buscar_producto(self,producto):
        self.verify_input_search()
        self.get_element(self._input_search).send_keys(producto)
        self.verify_button_search()
        self.get_element(self._button_search).click()
    
    def _get_featured_product(self,product):
        locator = f'//img[@title="{product}"]'
        featured_product = (By.XPATH, locator)
        return featured_product

    def verify_featured_product(self,option):
        assert self.is_displayed(self._get_featured_product(option)) , f'No en encuentra el producto {option} en el home'

    def select_feature_product(self,option):
        self.verify_featured_product(option)
        self.get_element(self._get_featured_product(option)).click()
