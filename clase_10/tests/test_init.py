

from selenium.webdriver.common.by import By
import clase_10.drivers.factory_driver as factory_driver
from clase_10.pages.home_page import HomePage
def test_init():
    driver = factory_driver.get_driver()
    home_page = HomePage(driver)
    search_locator = (By.XPATH, '//div[@id="search"]//button')
    home_page.is_display(search_locator)


