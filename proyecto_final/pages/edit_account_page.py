from proyecto_final.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class EditAccountPage(BasePage):

    _information_title = (By.XPATH, '//h1[text()="My Account Information"]')
    _firstname_input = (By.XPATH, '//input[@id="input-firstname"]')
    _lastname_input = (By.XPATH, '//input[@id="input-lastname"]')
    _email_input = (By.XPATH, '//input[@id="input-email"]')
    _telephone_input = (By.XPATH, '//input[@id="input-telephone"]')
    _continue_button = (By.XPATH, '//input[@type="submit"]')
    
    def __init__(self, driver) -> None:
        super().__init__(driver)
    
    def verify_my_account_information_page(self):
        assert self.is_displayed(self._information_title), 'No se encuentra el titulo Register Account en la pagina'
    
    def verify_input_firstname(self):
        assert self.is_displayed(self._firstname_input) , 'No en encuentra el campo First Name en la pagina'

    def write_firstname_value(self,text):
        self.verify_input_firstname()
        self.get_element(self._firstname_input).clear()
        self.get_element(self._firstname_input).send_keys(text)
    
    def verify_input_lastname(self):
        assert self.is_displayed(self._lastname_input) , 'No en encuentra el campo Last Name en la pagina'

    def write_lastname_value(self,text):
        self.verify_input_lastname()
        self.get_element(self._lastname_input).clear()
        self.get_element(self._lastname_input).send_keys(text)
    
    def verify_input_email(self):
        assert self.is_displayed(self._email_input) , 'No en encuentra el campo Email en la pagina'

    def write_email_value(self,text):
        self.verify_input_email()
        self.get_element(self._email_input).clear()
        self.get_element(self._email_input).send_keys(text)
    
    def verify_input_telephone(self):
        assert self.is_displayed(self._telephone_input) , 'No en encuentra el campo Telephone en la pagina'

    def write_telephone_value(self,text):
        self.verify_input_telephone()
        self.get_element(self._telephone_input).clear()
        self.get_element(self._telephone_input).send_keys(text)
    
    def verify_continue_button_clickable(self):
        self.verify_element_clickable(self._continue_button,5,'Boton Continue')

    def click_continue_button(self):
        self.verify_continue_button_clickable()
        self.get_element(self._continue_button).click()