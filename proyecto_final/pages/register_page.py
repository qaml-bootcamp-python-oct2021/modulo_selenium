from proyecto_final.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import proyecto_final.util.constants as constants


class RegisterPage(BasePage):
    _input_name = (By.ID, 'input-firstname')
    _input_last_name = (By.ID, 'input-lastname')
    _input_email = (By.ID, 'input-email')
    _input_tel = (By.ID, 'input-telephone')
    _input_pass = (By.ID, 'input-password')
    _input_confirm_pass = (By.ID, 'input-confirm')
    _check_privacy_policy = (By.XPATH, '//input[@name="agree"]')
    _btn_register = (By.XPATH, '//input[@type="submit"]')

    _alert_register_fail = (
        By.XPATH, ' //*[@id="account-register"]/div[@class="alert alert-danger alert-dismissible"]')

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def verify_input_name(self):
        assert self.is_displayed(
            self._input_name), 'No se encuentra el input  FirstName'

    def verify_input_last_name(self):
        assert self.is_displayed(
            self._input_last_name), 'No se encuentra el input  Last Name'

    def verify_input_tel(self):
        assert self.is_displayed(
            self._input_tel), 'No se encuentra el input  Telephone'

    def verify_input_email(self):
        assert self.is_displayed(
            self._input_email), 'No se encuentra el input  email'

    def verify_input_password(self):
        assert self.is_displayed(
            self._input_pass), 'No se encuentra el input  password'

    def verify_input_confirm_password(self):
        assert self.is_displayed(
            self._input_confirm_pass), 'No se encuentra el input confirm- password'

    def verify_check_agree(self):
        assert self.is_displayed(
            self._check_privacy_policy), 'No se encuentra el check  privacy policy'

    def verify_button_register(self):
        assert self.is_displayed(
            self._btn_register), 'No se encuentra el botón de Continue'

    def verify_alert_error(self):
        assert self.is_displayed(
            self._alert_register_fail), 'No se encuentra el mensaje de error'

    
    def verify_alert_error_text(self, text_expected):
        self.verify_alert_error()
        alert_text= self.get_element(self._alert_register_fail).text
        try:
            assert text_expected.strip() == alert_text.strip()
           
        except AssertionError:
            self.take_screenshot(constants.EVIDENCE_ERROR, f'register-alert')
            raise AssertionError(f'Alerta actual:{ alert_text}, alerta esperada: {text_expected}.')
    
    def write_name(self, name):
        self.verify_input_name()
        self.get_element(self._input_name).send_keys(name)

    def write_last_name(self, last_name):
        self.verify_input_last_name()
        self.get_element(self._input_last_name).send_keys(last_name)

    def write_email(self, email):
        self.verify_input_email()
        self.get_element(self._input_email).send_keys(email)

    def write_tel(self, tel):
        self.verify_input_tel()
        self.get_element(self._input_tel).send_keys(tel)

    def write_pass(self, password):
        self.verify_input_password()
        self.get_element(self._input_pass).send_keys(password)

    def write_confirm_pass(self, password):
        self.verify_input_confirm_password()
        self.get_element(self._input_confirm_pass).send_keys(password)

    def click_check_agree(self):
        self.verify_check_agree()
        self.click_element(self._check_privacy_policy)

    def click_continue(self):
        self.verify_button_register()
        self.click_element(self._btn_register)
