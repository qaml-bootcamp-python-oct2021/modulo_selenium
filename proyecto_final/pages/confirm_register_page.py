from proyecto_final.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ConfirmRegisterPage(BasePage):

    _confirm_title = (By.XPATH, '//div[@id="content"]//h1[text()="Your Account Has Been Created!"]')
    _continue_button = (By.XPATH, '//a[text()="Continue"]')

    def __init__(self, driver) -> None:
        super().__init__(driver)
    
    def verify_confirm_title(self):
        assert self.is_displayed(self._confirm_title), f'No se encuentra el titulo Your Account Has Been Created! en la pagina'


    def verify_continue_button_clickable(self):
        self.verify_element_clickable(self._continue_button,5,'Boton Continue')

    def click_continue_button(self):
        self.verify_continue_button_clickable()
        self.get_element(self._continue_button).click()