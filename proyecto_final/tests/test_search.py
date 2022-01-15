


from turtle import home
import proyecto_final.drivers.factory_driver as factory_driver

import pytest

from proyecto_final.pages.home_page import HomePage
from proyecto_final.pages.search_page import SearchPage
import proyecto_final.util.constants as constants


home_page: HomePage = None
search_page: SearchPage = None
def setup():
    driver=  factory_driver.get_driver()
    global home_page 
    home_page = HomePage(driver)
 
    
def test_no_search():
    home_page.search_producto("")
    home_page.verify_title_page("Your Store",constants.EVIDENCE_SEARCH )
    home_page.take_screenshot(constants.EVIDENCE_SEARCH, 'no_search')
  
   
def teardown():
    home_page.close_browser()

