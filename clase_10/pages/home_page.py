from clase_10.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    _logo = (By.ID, "logo")
    _input_search = (By.XPATH, '//input[@name="search"]')
    _button_search = (By.XPATH, '//div[@id="search"]//button')
    
    def __init__(self, driver) -> None:
         super().__init__(driver)

    def verify_logo(self):
        self.is_display(self._logo)
    
    def search(self,text):
        self.is_display(self._input_search)
        self._write(self._input_search,text)
        self.is_display(self._button_search)
        self._click(self._button_search)
