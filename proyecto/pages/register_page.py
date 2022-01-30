from selenium.webdriver.remote import webdriver
from proyecto.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class RegisterPage(BasePage):

    global name, lastname, email, telephone, pass1
    name = 'James'
    lastname = 'Harrison'
    email = 'jhm@outlook.com'
    telephone = '5589099817'
    pass1 = 'test'


    _my_account_button = (By.XPATH, '//span[@class="caret"]')
    _register_button = (By.XPATH, '//li//a[text() = "Register"]')
    _first_name_field = (By.ID,'input-firstname')
    _last_name_field = (By.ID, 'input-lastname')
    _email_field = (By.ID, 'input-email')
    _telephone_field = (By.ID, 'input-telephone')
    _pass_field = (By.ID, 'input-password')
    _confirm_pass_field = (By.ID, 'input-confirm')
    _agreed_checkbox = (By.XPATH, '//input[@type="checkbox"]')
    _submit_button = (By.XPATH, '//input[@type="submit"]')
    _successfull_reg_message = (By.XPATH, '//h1[text() = "Your Account Has Been Created!"]')


    def my_account_reg (self):
        self.verify_element_visible(self._my_account_button), 'No se encontrol el elemento'
        self.get_element(self._my_account_button).click()
        self.verify_element_visible(self._register_button), 'No se encontrio el elemento'
        self.get_element(self._register_button).click()
    
    def first_name_input (self):    
        self.verify_element_visible(self._first_name_field), 'No se encontro el campo First Name'
        self.get_element(self._first_name_field).send_keys(name)
    
    def last_name_input (self):
        self.verify_element_visible(self._last_name_field), 'No se encontro el campo last name'
        self.get_element(self._last_name_field).send_keys(lastname)
    
    def email_input (self):
        self.verify_element_visible(self._email_field), 'No se encontro el campo email'
        self.get_element(self._email_field).send_keys(email)
    
    def telephone_input (self):
        self.verify_element_visible(self._telephone_field), 'No se encontro el campo telephone'
        self.get_element(self._telephone_field).send_keys(telephone)
    
    def pass_input (self):
        self.verify_element_visible(self._pass_field), 'No se encontro el campo password'
        self.get_element(self._pass_field).send_keys(pass1)
    
    def confirm_input (self):
        self.verify_element_visible(self._confirm_pass_field), 'No se encontro el campo confirma password'
        self.get_element(self._confirm_pass_field).send_keys(pass1)
    
    def agree_checkbox (self):
        self.verify_element_visible(self._agreed_checkbox), 'No se encontro el checkbox'
        self.get_element(self._agreed_checkbox).click()
    
    def reg_confirmation (self):
        self.verify_element_visible(self._submit_button), 'No se encuentra el boton'
        self.get_element(self._submit_button).click()
    
    def conf_reg_success_message (self):
        self.verify_element_visible(self._successfull_reg_message), 'El mensaje no es el esperado'
        self.get_element(self._successfull_reg_message)
    