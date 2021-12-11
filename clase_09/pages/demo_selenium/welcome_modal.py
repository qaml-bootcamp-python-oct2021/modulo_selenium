from clase_09.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class WelcomeModal(BasePage):

    _close_icon = (By.ID,'at-cv-lightbox-close')

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def verify_close_icon(self,timeout):
        self.verify_element_visible(self._close_icon,timeout)

    def close_modal(self,timeout):
        self.verify_close_icon(timeout)
        self.get_element(self._close_icon).click()
