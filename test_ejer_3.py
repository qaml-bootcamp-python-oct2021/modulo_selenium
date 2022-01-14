from typing import ItemsView
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import selenium_driver
import time


driver : WebDriver = None

def setup():
    global driver
    browser = 'chrome'
    driver = selenium_driver.get_driver(browser)
    return driver

def test_search():
    url = 'https://laboratorio.qaminds.com/'
    usuario = 'testtt'
    password = 'tetttst'
    driver.get(url) 
    driver.maximize_window()

    my_account : WebElement = driver.find_element(By.XPATH, '//span[@class="caret"]')
    assert my_account.is_displayed(), 'No se encuentra el elemento'
    my_account.click()
    time.sleep(1)
    
    login_click : WebElement = driver.find_element(By.XPATH, '//li//a[text() = "Login"]')
    assert login_click.is_displayed(), 'No se encuentra el elemento'
    login_click.click()

    email_input : WebElement = driver.find_element(By.XPATH, '//input[@id="input-email"]')
    assert email_input.is_displayed(), 'No se encuentra el campo email'
    email_input.send_keys(usuario)
    
    pass_input : WebElement = driver.find_element(By.XPATH, '//input[@id="input-password"]')
    assert pass_input.is_displayed(), 'No se encuentra el campo password'
    pass_input.send_keys(password)

    login_click2 : WebElement = driver.find_element(By.XPATH, '//input[@value="Login"]')
    assert login_click2.is_displayed(), 'No se encuentra el boton login'
    login_click2.click()
    time.sleep(2)

    val_msj : WebElement = driver.find_element(By.XPATH, '//div[text()= " Warning: No match for E-Mail Address and/or Password."]')
    assert val_msj.is_displayed(), 'El mensaje no es correcto'


    time.sleep(2)


def teardown():
    driver.quit()