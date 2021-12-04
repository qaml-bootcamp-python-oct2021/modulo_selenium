from selenium.webdriver.remote.webdriver import WebDriver
import chrome_driver as chrome_driver
import firefox_driver as firefox_driver

def get_driver(browser_name) -> WebDriver :

    if browser_name == 'chrome':
        driver = chrome_driver.create_driver()
    elif browser_name == 'firefox':
        driver = firefox_driver.create_driver()
    else:
        raise Exception('Wrong driver')

    driver.implicitly_wait(20)
    driver.maximize_window()


    return driver