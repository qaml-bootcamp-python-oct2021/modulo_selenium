from proyecto_final.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ShoppingPage(BasePage):

    _shopping_title = (By.XPATH, '//div[@id="content"]//h1[contains(text(),"Shopping Cart")]')
    
    def __init__(self, driver) -> None:
        super().__init__(driver)
    
    def _get_product_image(self,product):
        locator = f'//table[@class="table table-bordered"]//img[@title="{product}"]'
        product_image = (By.XPATH, locator)
        return product_image
    
    def verify_product_image(self,product):
        assert self.is_displayed(self._get_product_image(product)), f'No se encuentra la imagen del producto {product} en la pagina'
    
    def _get_product_title(self,product):
        locator = f'//table[@class="table table-bordered"]//a[text()="{product}"]'
        product_title = (By.XPATH, locator)
        return product_title
    
    def verify_product_title(self,product):
        assert self.is_displayed(self._get_product_title(product)), f'No se encuentra la imagen del producto {product} en la pagina'
    
       
    def verify_shopping_title(self):
        assert self.is_displayed(self._shopping_title) , 'No se encuentra el titulo Shopping Cart en la pagina'

    def verify_shopping_page_with_product(self,product):
        self.verify_product_title(product)
        self.verify_product_image(product)
        self.verify_shopping_title()
    
    def vefify_shopping_page_empty(self):
       self.verify_shopping_title()