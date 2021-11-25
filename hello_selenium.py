import time
from selenium import webdriver

browser = 'firefox'

if browser == 'chrome':
    driver_path = './drivers/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)
elif browser == 'firefox':
    driver_path = './drivers/geckodriver.exe'
    driver = webdriver.Firefox(executable_path=driver_path)  
else: 
    raise RuntimeError ('No existe el driver del navegador indicado')

url = 'https://qamindslab.com/'

driver.get(url)
time.sleep(3)
driver.quit()
