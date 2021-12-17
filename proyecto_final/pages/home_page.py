from proyecto_final.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    _logo = ()

    
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def verify_logo (self):
        assert self._driver.find_element(By.XPATH, '//*[text()="About US"]').is_displayed()


