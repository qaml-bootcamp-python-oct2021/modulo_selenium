
from time import sleep
import pytest
import proyecto_final.drivers.factory_driver as factory_driver


from proyecto_final.pages.menu_page import MenuPage
from proyecto_final.pages.register_page import RegisterPage
import proyecto_final.util.data_handler as data
import proyecto_final.util.constants as constants
import time

menu_page: MenuPage = None
register_page: RegisterPage = None
def setup():
    driver=  factory_driver.get_driver()
    driver.get('https://laboratorio.qaminds.com/index.php?route=account/register')
    global register_page 
    register_page = RegisterPage(driver)
    


@pytest.mark.parametrize('name, last,email,tel, password',  data.get_data_csv(constants.DATA_USER_NEW))
def test_register_privacy_policy(name, last,email,tel, password):
    register_page.write_name(name)
    register_page.write_last_name(last)
    register_page.write_email(email)
    register_page.write_tel(tel)
    register_page.write_pass(password)
    register_page.write_confirm_pass(password)
    register_page.click_continue()
    register_page.verify_title_page('Register Account',constants.EVIDENCE_REGISTER)
    register_page.verify_alert_error_text("Warning: You must agree to the Privacy Policy!")
    register_page.take_screenshot(constants.EVIDENCE_REGISTER, f'register_privacy_policy_{name}')
  

def teardown():
    register_page.close_browser()

