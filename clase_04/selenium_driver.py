from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def get_driver():
    browser_firefox = False 
    if browser_firefox:
        driver_path = '../drivers/geckodriver.exe'
        options = Options()
        options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
        driver = webdriver.Firefox(options=options,executable_path=driver_path)
    else:
        driver_path = '../drivers/chromedriver.exe'
        driver = webdriver.Chrome(executable_path=driver_path)
    return driver