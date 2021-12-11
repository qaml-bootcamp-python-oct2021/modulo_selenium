from clase_09.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProgressBar(BasePage):

    _title = (By.XPATH,'//h2')
    _button_download = (By.ID,'downloadButton')
    _button_cancel_download = (By.XPATH,'//button[text()="Cancel Download"]')
    _dialog = (By.XPATH,'//div[@id="dialog"]//div[text()="Complete!"]')
    _button_close = (By.XPATH,'//button[text()="Close"]')

    def __init__(self, driver) -> None:
        super().__init__(driver)

    
    def verify_title(self):
        assert self.is_displayed(self._title) , 'No se encuentra el titulo de la pagina visible'

    def verify_title_text(self,expected_title):
        actual = self.get_element(self._title).text
        assert expected_title == actual , f'No coinciden los Titulos: Se esperaba {expected_title} y se obtuvo {actual}'

    def verify_start_download_button(self):
        assert self.is_displayed(self._button_download) , 'No se encuentra el boton "Start Download".'

    def verify_button_clickable(self):
        self.verify_element_clickable(self._button_download,5,'Boton Start Download')

    def click_on_start_download(self):
        self.verify_start_download_button()
        self.verify_button_clickable()
        self.get_element(self._button_download).click()

    def verify_cancel_button(self):
        assert self.is_displayed(self._button_cancel_download) , 'No se encuentra el boton "Cancel Download".'

    def verify_cancel_clickable(self):
        self.verify_element_clickable(self._button_cancel_download,5,'Boton Cancel Download')

    def verify_complete_message(self,timeout):
        self.verify_element_visible(self._dialog,timeout)

    def verify_close_button(self):
        assert self.is_displayed(self._button_download) , 'No se encuentra el boton "Close".'

    def verify_close_button_clickable(self):
        self.verify_element_clickable(self._button_download,5,'Boton Close')

    def click_on_close(self):
        self.verify_close_button()
        self.verify_close_button_clickable()
        self.get_element(self._button_close).click()