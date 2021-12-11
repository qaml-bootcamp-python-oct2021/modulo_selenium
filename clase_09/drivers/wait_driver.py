from selenium.webdriver.support.wait import WebDriverWait

def get_driver(driver,timeout) -> WebDriverWait:
    return WebDriverWait(driver,timeout)