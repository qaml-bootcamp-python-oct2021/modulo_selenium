from selenium.webdriver.remote import webdriver
from proyecto.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    global address, password
    address = 'record'
    password = 'breaker'
    
    _my_account_button = (By.XPATH, '//span[@class="caret"]')
    _my_account_login = (By.XPATH, '//li//a[text() = "Login"]')
    _email_address_input = (By.XPATH, '//input[@id="input-email"]')
    _password_input = (By.XPATH, '//input[@id="input-password"]')
    _login_button_myaccount = (By.XPATH, '//input[@value="Login"]')
    _forgot_pass_button = (By.XPATH, '//form//div//a[contains(text(),"Forgotten Password")]')
    _login_error_message = (By.XPATH, '//div[text()= " Warning: No match for E-Mail Address and/or Password."]')
    _welcome_message = (By.XPATH, '//div//h2[text() = "Returning Customer"]')

    def my_account_login (self):
        self.verify_element_visible(self._my_account_button), 'No se encontro el elemento'
        self.get_element(self._my_account_button).click()
        self.verify_element_visible(self._my_account_login), 'No se encontrio el elemento'
        self.get_element(self._my_account_login).click()
 
    def address_input (self):    
        self.verify_element_visible(self._email_address_input), 'No se encontro el campo email address'
        self.get_element(self._email_address_input).send_keys(address)
        
    def pass_input (self):    
        self.verify_element_visible(self._password_input), 'No se encontro el campo password'
        self.get_element(self._password_input).send_keys(password)

    def login_button (self):
        self.verify_element_visible(self._login_button_myaccount), 'No se encontro el boton'
        self.get_element(self._login_button_myaccount).click()
    
    def login_error_message(self):
        self.verify_element_visible(self._login_error_message), 'El mensaje de error no es correcto'
        self.get_element(self._login_error_message)

    def forgot_pass_link (self):
        self.verify_element_visible(self._forgot_pass_button), 'No se encuentra el link'
        self.get_element(self._forgot_pass_button)

    def welcome_message (self):
        self.verify_element_visible(self._welcome_message), 'El mensaje es incorrecto'
        self.get_element(self._welcome_message)
    