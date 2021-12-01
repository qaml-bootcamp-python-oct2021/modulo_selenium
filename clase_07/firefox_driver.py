from selenium.webdriver import Firefox

DRIVER_PATH = './drivers/geckodriver.exe'

def create_driver():

    driver = Firefox(executable_path=DRIVER_PATH)

    return driver