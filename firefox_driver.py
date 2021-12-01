from selenium.webdriver import Firefox

driver_path = './drivers/geckodriver.exe'

def create_driver():
    driver = Firefox(executable_path=driver_path)
    return driver