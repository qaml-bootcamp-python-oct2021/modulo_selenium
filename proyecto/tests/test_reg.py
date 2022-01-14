from proyecto.drivers import factory_driver
from proyecto.pages.home_page import HomePage
from proyecto.pages.register_page import RegisterPage
from proyecto.utils import data_handler
import time
import pytest

driver = None

def setup():
    global driver
    driver = factory_driver.get_driver()
    
def test_reg():
    reg_page = RegisterPage(driver)
    reg_page.my_account_reg()
    time.sleep(1)
    reg_page.first_name_input()
    reg_page.last_name_input()
    reg_page.email_input()
    reg_page.telephone_input()
    reg_page.pass_input()
    reg_page.confirm_input()
    reg_page.agree_checkbox()
    reg_page.take_screenshot()
    reg_page.reg_confirmation()
    reg_page.conf_reg_success_message()
    reg_page.take_screenshot()
    time.sleep(1)

def teardown():
    home_page = HomePage(driver)
    home_page.close_browser()