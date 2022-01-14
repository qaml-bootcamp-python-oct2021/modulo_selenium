from proyecto_final.drivers import factory_driver
from proyecto_final.pages.home_page import HomePage
from proyecto_final.pages.login_page import LoginPage
from proyecto_final.pages.logout_page import LogoutPage
from proyecto_final.pages.my_account_page import AccountPage
from proyecto_final.pages.top_bar_page import TopBar
from proyecto_final.utils import data_handler
import pytest

driver = None

def setup():
    global driver
    driver = factory_driver.get_driver()

@pytest.mark.parametrize('option,sub_option,email,password,sub_option2', [(data_handler.get_data('./proyecto_final/dataset/login.csv'))])
def test_login_logout(option,sub_option,email,password,sub_option2):
    top_bar = TopBar(driver)
    top_bar.select_option(option)
    top_bar.select_my_account_option(sub_option)
    login = LoginPage(driver)
    login.verify_login_page()
    login.write_email_value(email)
    login.write_password_value(password)
    login.click_login_button()
    my_account = AccountPage(driver)
    my_account.verify_account_page()
    my_account.take_screenshot()
    top_bar.select_option(option)
    top_bar.select_my_account_option(sub_option2)
    logout = LogoutPage(driver)
    logout.verify_logout_title()
    logout.take_screenshot()
    logout.click_continue_button()
    home = HomePage(driver)
    home.verify_home_page()
    
def teardown():
    TopBar(driver).close_browser()