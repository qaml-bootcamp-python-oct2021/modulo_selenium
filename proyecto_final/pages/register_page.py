from proyecto_final.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class RegisterPage(BasePage):

    _register_title = (By.XPATH, '//h1[text()="Register Account"]')
    _fielset = (By.ID, 'account')
    _firstname_input = (By.XPATH, '//input[@id="input-firstname"]')
    _lastname_input = (By.XPATH, '//input[@id="input-lastname"]')
    _email_input = (By.XPATH, '//input[@id="input-email"]')
    _telephone_input = (By.XPATH, '//input[@id="input-telephone"]')
    _password_input = (By.XPATH, '//input[@id="input-password"]')
    _confirm_input = (By.XPATH, '//input[@id="input-confirm"]')
    _agree_check =(By.XPATH,'//input[@name="agree"]')
    _continue_button = (By.XPATH, '//input[@type="submit"]')
    
    def __init__(self, driver) -> None:
        super().__init__(driver)
    
    def verify_register_title(self):
        assert self.is_displayed(self._register_title), 'No se encuentra el titulo Register Account en la pagina'

    def verify_fielset_account(self):
        assert self.is_displayed(self._fielset) , 'No se encuentra el campo Account en la pagina'
    
    def verify_register_page(self):
        self.verify_register_title()
        self.verify_fielset_account()

    def verify_input_firstname(self):
        assert self.is_displayed(self._firstname_input) , 'No en encuentra el campo First Name en la pagina'

    def write_firstname_value(self,text):
        self.verify_input_firstname()
        self.get_element(self._firstname_input).send_keys(text)
    
    def verify_input_lastname(self):
        assert self.is_displayed(self._lastname_input) , 'No en encuentra el campo Last Name en la pagina'

    def write_lastname_value(self,text):
        self.verify_input_lastname()
        self.get_element(self._lastname_input).send_keys(text)
    
    def verify_input_email(self):
        assert self.is_displayed(self._email_input) , 'No en encuentra el campo Email en la pagina'

    def write_email_value(self,text):
        self.verify_input_email()
        self.get_element(self._email_input).send_keys(text)
    
    def verify_input_telephone(self):
        assert self.is_displayed(self._telephone_input) , 'No en encuentra el campo Telephone en la pagina'

    def write_telephone_value(self,text):
        self.verify_input_telephone()
        self.get_element(self._telephone_input).send_keys(text)
    
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
    
    def _get_option(self,option):
        if option == "yes":
            locator = f'//input[@name="newsletter" and @value="1"]'
            subscribe_option = (By.XPATH, locator)
            return subscribe_option
        else:
            locator = f'//input[@name="newsletter" and @value="0"]'
            subscribe_option = (By.XPATH, locator)
            return subscribe_option

    def verify_suscribe_option(self,option):
        assert self.is_displayed(self._get_option(option)) , 'No en encuentra la opcion {option} en la pagina'

    def subscribe_option(self,option):
        self.verify_suscribe_option(option)
        self.get_element(self._get_option(option)).click()
    
    def verify_check_box_clickable(self):
        self.verify_element_clickable(self._agree_check,5,'Box Agree')

    def select_check(self):
        self.verify_check_box_clickable()
        self.get_element(self._agree_check).click()
    
    def verify_continue_button_clickable(self):
        self.verify_element_clickable(self._continue_button,5,'Boton Continue')

    def click_continue_button(self):
        self.verify_continue_button_clickable()
        self.get_element(self._continue_button).click()
