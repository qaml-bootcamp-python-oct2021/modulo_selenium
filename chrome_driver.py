from selenium.webdriver import Chrome

driver_path = './drivers/chromedriver.exe'

def create_driver():
    driver = Chrome(executable_path=driver_path)
    return driver