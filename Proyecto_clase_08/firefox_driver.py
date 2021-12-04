from selenium.webdriver import Firefox , FirefoxOptions , FirefoxProfile
import config_handler

FIREFOX_PRIVATE = 'browser.privatebrowsing.autostart'

def create_driver():
    ff_options = FirefoxOptions()
    ff_profile = FirefoxProfile()
    ff_profile.set_preference(FIREFOX_PRIVATE,config_handler.get_incognito_mode())
    ff_options.headless = config_handler.get_headless_mode()
    driver = Firefox(options=ff_options,firefox_profile=ff_profile,executable_path=config_handler.get_driver_path())
    return driver