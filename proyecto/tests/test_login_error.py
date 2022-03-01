from proyecto.drivers import factory_driver
from proyecto.pages.home_page import HomePage
from proyecto.pages.login_page import LoginPage

driver = None

def setup():
    global driver
    driver = factory_driver.get_driver()

def test_my_account():
    login_page = LoginPage(driver)
    login_page.my_account_login()
    login_page.address_input()
    login_page.pass_input()
    login_page.login_button()
    login_page.login_error_message()
    login_page.take_screenshot()

def test_forgot_passLink():
    link_forgot = LoginPage (driver)
    link_forgot.my_account_login()
    link_forgot.forgot_pass_link()
    
def teardown():
    home_page = HomePage(driver)
    home_page.close_browser()
