
from time import sleep
import pytest
import proyecto_final.drivers.factory_driver as factory_driver


from proyecto_final.pages.menu_page import MenuPage
from proyecto_final.pages.login_page import LoginPage
import proyecto_final.util.data_handler as data
import proyecto_final.util.constants as constants
import time

menu_page: MenuPage = None
login_page: LoginPage = None
def setup():
    driver=  factory_driver.get_driver()
    driver.get('https://laboratorio.qaminds.com/index.php?route=account/login')
    global login_page 
    login_page = LoginPage(driver)
    global menu_page 
    menu_page = MenuPage(driver)


@pytest.mark.parametrize('email, password',  data.get_data_csv(constants.DATA_USER_VALID))
def test_login_success(email,password):
    login_page.write_email(email)
    login_page.write_password(password)
    login_page.click_login()
    login_page.verify_title_page('My Account',constants.EVIDENCE_LOGIN)
    menu_page.click_menu('My Account')
    menu_page.verify_submenu('Logout')
    login_page.take_screenshot(constants.EVIDENCE_LOGIN, f'login_success_{email}')

@pytest.mark.parametrize('email, password',  data.get_data_csv(constants.DATA_USER_INVALID))
def test_login_fail(email,password):
    login_page.write_email(email)
    login_page.write_password(password)
    login_page.click_login()
    login_page.verify_title_page('Account Login',constants.EVIDENCE_LOGIN)
    login_page.verify_alert_error()
    login_page.take_screenshot(constants.EVIDENCE_LOGIN, f'login_fail_{email}')
   

def teardown():
    login_page.close_browser()

