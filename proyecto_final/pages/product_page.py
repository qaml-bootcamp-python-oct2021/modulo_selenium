from proyecto_final.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):

    _input_quantity = (By.ID, 'input-quantity')
    _select_option = (By.ID, 'input-option226')
    _button_cart = (By.ID, 'button-cart')
    _menssage_alert = (By.CSS_SELECTOR, '.alert.alert-success.alert-dismissible')
    _shopping_cart_link = (By.XPATH, '//a[text()="shopping cart"]')

    def __init__(self,driver) -> None:
        super().__init__(driver)
    
    def _get_product_image(self,product):
        locator = f'(//img[@title="{product}"])[1]'
        product_image = (By.XPATH, locator)
        return product_image
    
    def verify_product_image(self,product):
        assert self.is_displayed(self._get_product_image(product)), f'No se encuentra la imagen del producto {product} en la pagina'
    
    def _get_product_title(self,product):
        locator = f'//h1[contains(text(),"{product}")]'
        product_title = (By.XPATH, locator)
        return product_title
    
    def verify_product_title(self,product):
        assert self.is_displayed(self._get_product_title(product)), f'No se encuentra la imagen del producto {product} en la pagina'
    
    def verify_product_page(self,product):
        self.verify_product_title(product)
        self.verify_product_image(product)
    
    def verify_select(self):
        assert self.is_displayed(self._select_option), 'No se encuentra el selector en la pagina'

    def select_available_option(self,option):
        self.verify_select()
        self.select_element_list(self._select_option,option)
    
    def verify_input_quantity(self):
        assert self.is_displayed(self._input_quantity), 'No se encuentra el campo cantidad en la pagina'
    
    def write_quantity_value(self,quantity=1):
        self.verify_input_quantity()
        self.get_element(self._input_quantity).clear()
        self.get_element(self._input_quantity).send_keys(quantity)
    
    def verify_button_cart(self):
        self.verify_element_clickable(self._button_cart,10,'Boton Add to Cart')
    
    def click_button_cart(self):
        self.verify_button_cart()
        self.get_element(self._button_cart).click()
        self.verify_button_cart()
    
    def verify_menssage_alert(self):
        self.verify_element_visible(self._menssage_alert,5)
    
    def verify_shopping_cart_link_clickable(self):
        self.verify_element_clickable(self._shopping_cart_link,5,'link shopping cart') 
    
    def click_shopping_cart_link(self):
        self.verify_shopping_cart_link_clickable()
        self.get_element(self._shopping_cart_link).click()