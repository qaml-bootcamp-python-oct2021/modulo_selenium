from clase_09.drivers import factory_driver
import time
import pytest
from clase_09.utils import data_handler
from clase_09.pages.demo_selenium.welcome_modal import WelcomeModal
from clase_09.pages.demo_selenium.nav_bar import NavBar
from clase_09.pages.demo_selenium.nav_progress_bar import NavProgressBar
from clase_09.pages.demo_selenium.progress_bar import ProgressBar

driver = None

def setup():
    global driver
    driver = factory_driver.get_driver()

@pytest.mark.parametrize('option,sub_option,title',[('Progress Bars','JQuery Download Progress bars','JQuery UI Progress bar - Download Dialog')])
def test_start_download(option,sub_option,title):
    welcome_modal = WelcomeModal(driver)
    welcome_modal.close_modal(10)
    nav_bar = NavBar(driver)
    nav_bar.select_option(option)
    nav_progress_bar = NavProgressBar(driver)
    nav_progress_bar.select_option(sub_option)
    progress_bar = ProgressBar(driver)
    progress_bar.verify_title()
    progress_bar.verify_title_text(title)
    progress_bar.click_on_start_download()
    progress_bar.verify_cancel_button()
    progress_bar.verify_cancel_clickable()
    progress_bar.take_screenshot('Inicio_Descarga')
    progress_bar.verify_complete_message(5)
    progress_bar.take_screenshot('Descarga_Completa')
    progress_bar.click_on_close()
    progress_bar.take_screenshot('Fin_Test_Start_Download')


def teardown():
    WelcomeModal(driver).close_browser()