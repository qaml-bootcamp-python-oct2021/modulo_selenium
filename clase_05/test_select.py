from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import selenium_driver
import time

driver : WebDriver = None

url = 'https://demoqa.com/select-menu'

def setup():
    global driver
    driver = selenium_driver.get_driver('chrome')
    driver.maximize_window()
    driver.get(url)
    

# def test_select_by_text():
#     option = 'Voilet'
#     select : WebElement = driver.find_element(By.ID,'oldSelectMenu')
#     assert select.is_displayed() , 'No se encuentra el selector'
#     option_list = Select(select)
#     option_list.select_by_visible_text(option)
#     time.sleep(5)
    

# def test_select_by_value():
#     option = '8'
#     select : WebElement = driver.find_element(By.ID,'oldSelectMenu')
#     assert select.is_displayed() , 'No se encuentra el selector'
#     option_list = Select(select)
#     option_list.select_by_value(option)
#     time.sleep(5)
    
# def test_select_by_index():
#     option = '3'
#     select : WebElement = driver.find_element(By.ID,'oldSelectMenu')
#     assert select.is_displayed() , 'No se encuentra el selector'
#     option_list = Select(select)
#     option_list.select_by_index(option)
#     time.sleep(5)

def test_ejercicio5():
    option_data = 'A root option'
    select : WebElement = driver.find_element(By.ID,'withOptGroup')
    assert select.is_displayed() , 'No se encuentra el selector'
    select.click()
    option_xpath = f'//*[text()="{option_data}"]'
    option : WebElement = driver.find_element(By.XPATH,option_xpath)
    assert option.is_displayed() , f'No se encuentra la opcion {option_data}'
    option.click()
    selected_option : WebElement = driver.find_element(By.XPATH,option_xpath)
    assert option_data == selected_option.text , f'La opcion seleccionada no coincide, esperaba {option_data} y se obtuvo {selected_option.text}'
    time.sleep(3)

def teardown():
    driver.quit()