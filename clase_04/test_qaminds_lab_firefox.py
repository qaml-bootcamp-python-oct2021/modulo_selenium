from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import factory_driver as fd

driver : WebDriver = None

def setup():
    global driver 
    driver = fd.get_driver('firefox')
    driver.get('https://laboratorio.qaminds.com/')

def test_iphone_search():
    producto = "iphone"
    driver.maximize_window()
    search_bar : WebElement = driver.find_element(By.XPATH,'//input[@name="search"]')
    assert search_bar.is_displayed(), 'No se encuentra la barra de busqueda'
    search_bar.send_keys(producto)
    search_bar.send_keys(Keys.ENTER)
    iphone_img : WebElement = driver.find_element(By.XPATH,f'//img[contains(@src,"{producto}")]')
    assert iphone_img.is_displayed(), f'No se encuentra la imagen del producto \'{producto}\''

def test_samsung_search():
    producto = "samsung"
    driver.maximize_window()
    search_bar : WebElement = driver.find_element(By.XPATH,'//input[@name="search"]')
    assert search_bar.is_displayed(), 'No se encuentra la barra de busqueda'
    search_bar.send_keys(producto)
    search_bar.send_keys(Keys.ENTER)
    iphone_img : WebElement = driver.find_element(By.XPATH,f'//img[contains(@src,"{producto}")]')
    assert iphone_img.is_displayed(), f'No se encuentra la imagen del producto \'{producto}\''
    
def test_tablet_search():
    producto = "tablet"
    driver.maximize_window()
    search_bar : WebElement = driver.find_element(By.XPATH,'//input[@name="search"]')
    assert search_bar.is_displayed(), 'No se encuentra la barra de busqueda'
    search_bar.send_keys(producto)
    search_bar.send_keys(Keys.ENTER)
    iphone_img : WebElement = driver.find_element(By.XPATH,f'//img[contains(@src,"{producto}")]')
    assert iphone_img.is_displayed(), f'No se encuentra la imagen del producto \'{producto}\''

def teardown():
    driver.quit()