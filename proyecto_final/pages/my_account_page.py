from proyecto_final.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class AccountPage(BasePage):

    _my_account_title = (By.XPATH,'//h2[text()="My Account"]')
    _my_orders_title = (By.XPATH,'//h2[text()="My Orders"]')
    _my_affiliate_account_title =(By.XPATH,'//h2[text()="My Affiliate Account"]')
    _new_newsletter_title =(By.XPATH,'//h2[text()="Newsletter"]')
    _edit_account_link =(By.XPATH,'//a[contains(text(),"Edit your account")]')
    _change_pass_link = (By.XPATH,'//a[text()="Change your password"]')
    _menssage_succes = (By.CSS_SELECTOR, '.alert.alert-success.alert-dismissible')

    def __init__(self, driver) -> None:
        super().__init__(driver)
    
    def verify_my_account_title(self):
        assert self.is_displayed(self._my_account_title) , 'No se encuentra el titulo My Account en la pagina'
    
    def verify_my_orders_title(self):
        assert self.is_displayed(self._my_orders_title) , 'No se encuentra el titulo My Orders en la pagina'
    
    def verify_my_affiliate_account_title(self):
        assert self.is_displayed(self._my_affiliate_account_title) , 'No se encuentra el titulo My Affiliate Account en la pagina'
    
    def verify_account_page(self):
        self.verify_my_account_title()
        self.verify_my_affiliate_account_title()
        self.verify_my_orders_title()
        self.verify_new_newsletter_title()
        
    def verify_new_newsletter_title(self):
        assert self.is_displayed(self._new_newsletter_title) , 'No se encuentra el titulo Newsletter en la pagina'
    
    def verify_edit_account_link(self):
        assert self.is_displayed(self._edit_account_link) , 'No se encuentra el link Edit your account information en la pagina'
    
    def click_edit_account(self):
        self.verify_edit_account_link()
        self.get_element(self._edit_account_link).click()
    
    def verify_change_password_link(self):
        assert self.is_displayed(self._change_pass_link) , 'No se encuentra el link Change Password en la pagina'
    
    def click_change_password(self):
        self.verify_change_password_link()
        self.get_element(self._change_pass_link).click()
    
    def verify_menssage_alert(self):
        self.verify_element_visible(self._menssage_succes,5)