from proyecto_final.drivers import factory_driver
from proyecto_final.pages.change_pass_page import ChangePasswordPage
from proyecto_final.pages.edit_account_page import EditAccountPage
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

@pytest.mark.parametrize('option,sub_option,email,password,new_name,new_lastname,new_email,new_telephone,new_password,sub_option2', [(data_handler.get_data('./proyecto_final/dataset/login_and_new_data.csv'))])
def test_edit_info_pass(option,sub_option,email,password,new_name,new_lastname,new_email,new_telephone,new_password,sub_option2):
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
    my_account.click_edit_account()
    edit_info = EditAccountPage(driver)
    edit_info.verify_my_account_information_page()
    edit_info.write_firstname_value(new_name)
    edit_info.write_lastname_value(new_lastname)
    edit_info.write_email_value(new_email)
    edit_info.write_telephone_value(new_telephone)
    edit_info.click_continue_button()
    my_account.take_screenshot()
    my_account.verify_account_page()
    my_account.verify_menssage_alert()
    my_account.click_change_password()
    change_pass = ChangePasswordPage(driver)
    change_pass.verify_change_pass_page()
    change_pass.write_password_value(new_password)
    change_pass.write_confirm_value(new_password)
    change_pass.click_continue_button()
    my_account.take_screenshot()
    my_account.verify_account_page()
    my_account.verify_menssage_alert()
    top_bar.select_option(option)
    top_bar.select_my_account_option(sub_option2)
    logout = LogoutPage(driver)
    logout.verify_logout_title()
    logout.click_continue_button()
    home = HomePage(driver)
    home.verify_home_page()
    top_bar = TopBar(driver)
    top_bar.select_option(option)
    top_bar.select_my_account_option(sub_option)
    login = LoginPage(driver)
    login.verify_login_page()
    login.write_email_value(new_email)
    login.write_password_value(new_password)
    login.click_login_button()
    my_account = AccountPage(driver)
    my_account.verify_account_page()
    
    
    
def teardown():
    TopBar(driver).close_browser()