from proyecto_final.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import proyecto_final.util.constants as constants

class LoginPage(BasePage):
    _input_email =  (By.ID, 'input-email')
    _input_pass =  (By.ID, 'input-password')
    _btn_login= (By.XPATH, '//input[@type="submit"]')
    _alert_login_fail= (By.XPATH, ' //*[@id="account-login"]/div[@class="alert alert-danger alert-dismissible"]')
      

    
    def __init__(self, driver) -> None:
         super().__init__(driver)
    
    def verify_input_email(self):
        assert self.is_displayed(self._input_email) , 'No se encuentra el input de email'

    def verify_input_password(self):
        assert self.is_displayed(self._input_pass) , 'No se encuentra el input de password'

    def verify_button_login(self): 
        assert self.is_displayed(self._btn_login) , 'No se encuentra el botón de Login'
    
    def verify_alert_error(self):
        assert self.is_displayed(self._alert_login_fail) , 'No se encuentra el mensaje de error'

    def write_email(self, email):
        self.verify_input_email()
        self.write_text_element(self._input_email, email)
    
    def write_password(self, password):
        self.verify_input_password()
        self.write_text_element(self._input_pass, password)
    
      
    def click_login(self):
        self.verify_button_login()
        self.click_element(self._btn_login)
    
  
    
  
  
  
 

