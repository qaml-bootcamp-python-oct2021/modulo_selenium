import time
import pytest
import selenium_driver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

driver :WebDriver = None
def setup():
    global driver
    driver = selenium_driver.get_driver()

def test_menu_window():
    global driver
    url_pag ='https://laboratorio.qaminds.com/'
    driver.get(url_pag)
    current_url= driver.current_url
    assert url_pag == current_url, f'Url no coinciden,  actual:{current_url} buscada:{url_pag}'
    
    name_menu = "Laptops & Notebooks"
    menu: WebElement = driver.find_element(By.XPATH, f'//nav[@id="menu"]//a[contains(text(), "{name_menu}")]')
    assert menu.is_displayed, f'No se encuentra el menú {name_menu}'
    menu.click()
    name_submenu = "Windows"
    submenu: WebElement = driver.find_element(By.XPATH, f'//nav[@id="menu"]//a[contains(text(), "{name_submenu}")]')
    assert submenu.is_displayed, f'No se encuentra el submenú {name_submenu}'

    submenu.click()

    msg_empty = "There are no products"
    msg_item: WebElement = driver.find_element(By.XPATH, f'//div[@id="content"]//p[contains(text(), "{msg_empty}")]')
    assert msg_item.is_displayed, 'Existen productos'
    
    name_btn ='Continuar'
    continuar_btn: WebElement = driver.find_element(By.XPATH, f'//div[@id="content"]//a [contains(text(), "{name_btn}")]')
    time.sleep(3)
    assert continuar_btn.is_displayed, f'Botón {name_btn} no encontrado'
    continuar_btn.click()
    title_home ="Your Store"
    assert title_home == driver.title, f'El botón {name_btn} no redirigio a la pantalla de inicio'

   


def teardown():
    driver.quit()