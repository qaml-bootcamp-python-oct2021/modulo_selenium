from clase_09.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class NavProgressBar(BasePage):

    
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def _get_menu_option(self,option):
        locator = f'//div[@id="navbar-brand-centered"]//a[contains(text() , "{option}")]'
        menu_option = (By.XPATH,locator)
        return menu_option

    def verify_menu_option(self,option):
        assert self.is_displayed(self._get_menu_option(option)) , f'No en encuentra la opcion {option} en el menu'

    def select_option(self,option):
        self.verify_menu_option(option)
        self.get_element(self._get_menu_option(option)).click()