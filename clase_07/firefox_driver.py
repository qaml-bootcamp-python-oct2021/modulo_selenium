from selenium.webdriver import Firefox

DRIVER_PATH = './driver/geckodriver.exe'

def create_driver():
    driver = Firefox(executable_path=DRIVER_PATH)
    return driver