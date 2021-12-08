
from selenium.webdriver import Firefox , FirefoxOptions , FirefoxProfile
import clase_10.util.config_handler as config

FIREFOX_PRIVATE = 'browser.privatebrowsing.autostart'
def create_driver ():

        options = FirefoxOptions()
        options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
        options.headless = config.get_headless_mode()

        profile = FirefoxProfile()
        profile.set_preference(FIREFOX_PRIVATE,config.get_incognito_mode())
     
        driver = Firefox(options=options,firefox_profile=profile,executable_path=config.get_driver())
        return driver