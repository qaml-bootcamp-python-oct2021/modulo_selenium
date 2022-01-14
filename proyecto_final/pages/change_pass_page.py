from proyecto_final.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ChangePasswordPage(BasePage):
    
    _change_pass_title = (By.XPATH, '//h1[text()="Change Password"]')
    _password_input = (By.XPATH, '//input[@id="input-password"]')
    _confirm_input = (By.XPATH, '//input[@id="input-confirm"]')
    _continue_button = (By.XPATH, '//input[@type="submit"]')
    
    def __init__(self, driver) -> None:
        super().__init__(driver)
    
    def verify_change_pass_page(self):
        assert self.is_displayed(self._change_pass_title), 'No se encuentra el titulo Register Account en la pagina'
    
    def verify_input_password(self):
        assert self.is_displayed(self._password_input) , 'No en encuentra el campo Password en la pagina'

    def write_password_value(self,text):
        self.verify_input_password()
        self.get_element(self._password_input).send_keys(text)
    
    def verify_input_confirm(self):
        assert self.is_displayed(self._confirm_input) , 'No en encuentra el campo Password Confirm en la pagina'

    def write_confirm_value(self,text):
        self.verify_input_confirm()
        self.get_element(self._confirm_input).send_keys(text)

    def verify_continue_button_clickable(self):
        self.verify_element_clickable(self._continue_button,5,'Boton Continue')

    def click_continue_button(self):
        self.verify_continue_button_clickable()
        self.get_element(self._continue_button).click()