import pytest
from proyecto_final.pages.base_page import BasePage
from proyecto_final.pages.confirm_register_page import ConfirmRegisterPage
from proyecto_final.pages.home_page import HomePage
from proyecto_final.pages.my_account_page import AccountPage
from proyecto_final.pages.top_bar_page import TopBar
from proyecto_final.pages.register_page import RegisterPage
from proyecto_final.drivers import factory_driver
from proyecto_final.utils import data_handler
import time

driver = None

def setup():
    global driver
    driver = factory_driver.get_driver()

@pytest.mark.parametrize('option,sub_option,firstname,lastname,email,telephone,password,subscribe', [(data_handler.get_data('./proyecto_final/dataset/register.csv'))])
def test_register(option,sub_option,firstname,lastname,email,telephone,password,subscribe):
    top_bar = TopBar(driver)
    top_bar.select_option(option)
    top_bar.select_my_account_option(sub_option)
    register = RegisterPage(driver)
    register.verify_register_page()
    register.write_firstname_value(firstname)
    register.write_lastname_value(lastname)
    register.write_email_value(email)
    register.write_telephone_value(telephone)
    register.write_password_value(password)
    register.write_confirm_value(password)
    register.subscribe_option(subscribe)
    register.select_check()
    register.click_continue_button()
    confirm_register = ConfirmRegisterPage(driver)
    confirm_register.verify_confirm_title()
    confirm_register.take_screenshot()
    confirm_register.click_continue_button()
    my_account = AccountPage(driver)
    my_account.verify_account_page()


def teardown():
    TopBar(driver).close_browser()