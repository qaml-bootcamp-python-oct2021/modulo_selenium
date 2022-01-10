from proyecto_final.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    _logo = (By.XPATH, '//div[@id="logo"]//img')

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def verify_logo(self):
        assert self.is_displayed(self._logo) , 'No se encontro el logo'

    def click_logo (self):
        self.get_element(self._logo).click()


         