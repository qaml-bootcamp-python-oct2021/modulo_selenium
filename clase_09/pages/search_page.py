from clase_09.pages.base_page import BasePage

class SearchPage(BasePage):
    
    def __init__(self, driver) -> None:
        super().__init__(driver)