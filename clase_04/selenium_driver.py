from selenium import webdriver

def get_driver(browser):
    if browser == 'chrome':
        driver_path = './drivers/chromedriver.exe'
        driver = webdriver.Chrome(executable_path=driver_path)
    else:
        raise RuntimeError('No existe el driver del navegador seleccionado')
    return driver