from selenium.webdriver import Chrome

DRIVER_PATH = './driver/chromedriver.exe'

def create_driver():
    driver = Chrome(executable_path=DRIVER_PATH)
    return driver