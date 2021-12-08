from clase_10.pages.base_page import BasePage


class HomePage(BasePage):
    _logo = ()
    
    def __init__(self, driver) -> None:
         super().__init__(driver)
    

