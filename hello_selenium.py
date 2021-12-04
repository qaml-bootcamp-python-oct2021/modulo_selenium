import time
from selenium import webdriver

browser = 'firefox'

if bowser == 'chrome':
    driver_path = './drivers/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)
elif browser == 'firefox'
    driver_path = './drivers/geckodriver.exe'
    driver = webdriver.Firefox(executable_path=driver_path)
else:
    raise RuntimeError ('No hay driver para ese navegador')

url = 'httos://qamindslab.com'

driver.get(url)
time.sleep(3)
driver.quit()