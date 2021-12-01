from selenium import webdriver
import firefox_driver
import chrome_driver
FIREFOX= '0'
CHROME= '1'
def get_driver(browser):
    if browser == FIREFOX:
        driver = firefox_driver.create_driver()
    elif browser == CHROME:
        driver = chrome_driver.create_driver()
    else:
        raise Exception('No found driver')
    return driver