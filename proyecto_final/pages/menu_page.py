from proyecto_final.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import proyecto_final.util.constants as constants

class MenuPage(BasePage):
 
    

    
    def __init__(self, driver) -> None:
         super().__init__(driver)

    def _get_locator_menu(self, menu):
        return (By.XPATH,f' //*[@id="top-links"]//span[contains (text(),"{menu}")]')
    def _get_locator_submenu(self, submenu):
        return (By.XPATH,f' //*[@id="top-links"]//a[contains (text(),"{submenu}")]')
    def verify_menu(self,menu):
        assert self.is_displayed(self._get_locator_menu(menu)) , f'No se encuentra el menu:{menu}'
  
    def click_menu(self, menu):
       self.verify_menu(menu)
       self.click_element(self._get_locator_menu(menu))
    
    def verify_submenu(self, submenu):
        assert self.is_displayed(self._get_locator_submenu(submenu)) , f'No se encuentra el submenu:{submenu}'
     


