from selenium.webdriver.remote.webdriver import WebDriver
from proyecto_final.drivers import chrome_driver , firefox_driver
from proyecto_final.utils import config_handler


def get_driver():
    config_handler.load_config()
    browser = config_handler.get_browser_name()
    
    if browser == 'chrome':
        driver = chrome_driver.create_driver()
    elif browser == 'firefox':
        driver = firefox_driver.create_driver()
    else:
        raise RuntimeError('No existe el driver del navegador indicado')
    
    if config_handler.get_headless_mode():
        driver.set_window_size(config_handler.get_headless_resolution['width'],config_handler.get_headless_resolution['height'])
    else:
        driver.maximize_window()
    
    if config_handler.get_implicit_wait_time():
        driver.implicitly_wait(config_handler.get_implicit_wait_time())
    
    driver.set_page_load_timeout(config_handler.get_page_load())
    
    driver.get(config_handler.get_url_app())

    

    return driver