from selenium.webdriver.remote.webdriver import WebDriver
import chrome_driver , firefox_driver

def get_driver(browser):
    if browser == 'chrome':
        driver = chrome_driver.create_driver()
    elif browser == 'firefox':
        driver = firefox_driver.create_driver()
    else:
        raise RuntimeError('No existe el driver del navegador indicado')
    
    driver.maximize_window()
    driver.implicitly_wait(3)
    return driver