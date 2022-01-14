from proyecto_final.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    _new_customer_title =(By.XPATH,'//h2[text()="New Customer"]')
    _returning_customer_title = (By.XPATH,'//h2[text()="Returning Customer"]')
    _continue_button = (By.XPATH,'//a[text()="Continue"]')
    _email_input = (By.ID,'input-email')
    _password_input = (By.ID,'input-password')
    _login_button = (By.XPATH,'//input[@type="submit"]')

    def __init__(self, driver) -> None:
        super().__init__(driver)
    
    def verify_new_customer_title(self):
        assert self.is_displayed(self._new_customer_title) , 'No se encuentra el titulo New Customer en la pagina'
    
    def verify_returning_customer_title(self):
        assert self.is_displayed(self._returning_customer_title) , 'No se encuentra el titulo Returning Customer en la pagina'

    def verify_login_page(self):
        self.verify_new_customer_title()
        self.verify_returning_customer_title()

    def verify_input_email(self):
        assert self.is_displayed(self._email_input) , 'No en encuentra el campo Email en la pagina'

    def write_email_value(self,text):
        self.verify_input_email()
        self.get_element(self._email_input).send_keys(text)
    
    def verify_input_password(self):
        assert self.is_displayed(self._password_input) , 'No en encuentra el campo Password en la pagina'

    def write_password_value(self,text):
        self.verify_input_password()
        self.get_element(self._password_input).send_keys(text)
    
    def verify_login_button_clickable(self):
        self.verify_element_clickable(self._login_button,5,'Boton Login')

    def click_login_button(self):
        self.verify_login_button_clickable()
        self.get_element(self._login_button).click()