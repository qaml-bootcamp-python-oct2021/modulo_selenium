from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium_driver
import time
import pytest

#ejercicio clase 4_02 - buscar tablets, luego samsung galaxy, verificar precio, agregar al carrito y accesar carrito

driver : WebDriver = None

def setup():
    global driver
    browser = 'chrome'
    driver = selenium_driver.get_driver(browser)
    url = 'https://laboratorio.qaminds.com/'
    driver.get(url)

def login():
    #go to login page
    my_acct_menu_opt : WebElement = driver.find_element(By.XPATH,'//li//a[@title = "My Account"]')
    assert my_acct_menu_opt.is_displayed(), 'No se encuentra la opcion de My Account'
    my_acct_menu_opt.click()
    time.sleep(3)
    login_menu_opt : WebElement = driver.find_element(By.XPATH,'//li//a[text() = "Login"]')
    assert login_menu_opt.is_displayed(), 'No se encuentra la opcion de Login'
    login_menu_opt.click()
    time.sleep(3)

    #enter credentials
    username_field : WebElement = driver.find_element(By.XPATH,'//input[@id = "input-email"]')
    assert username_field.is_displayed(), 'No se encuentra el campo de e-mail address'
    username_field.send_keys('tonycol1984@gmail.com')
    password_field : WebElement = driver.find_element(By.XPATH,'//input[@id = "input-password"]')
    assert password_field.is_displayed(), 'No se encuentra el campo de password'
    password_field.send_keys('python48')
    login_btn : WebElement = driver.find_element(By.XPATH,'//input[@type = "submit"]')
    assert login_btn.is_displayed(), 'No se encuentra el boton de Login'
    login_btn.click()
    time.sleep(1)


def limpiar_carrito():
    #Click en boton de carrito
    shopping_cart_button: WebElement = driver.find_element(By.XPATH,f'//span[@id = "cart-total"]')
    assert shopping_cart_button.is_displayed(), 'Shopping Cart button no se ha encontrado'
    shopping_cart_button.click()
    time.sleep(2)

    remove_item: WebElement = driver.find_element(By.XPATH, '//button[@title = "Remove"]')
    assert remove_item.is_displayed(), 'El boton para eliminar item no se encuentra'
    remove_item.click()
    time.sleep(2)

    shopping_cart_button= driver.find_element(By.XPATH,f'//span[@id = "cart-total" and contains(text(),"$0.00")]')
    assert shopping_cart_button.is_displayed(), 'El carrito no ha sido vaciado'
    time.sleep(1)

def limpiar_wishlist():

    wishlist_link : WebElement = driver.find_element(By.XPATH, '//li//a[text() = "Wish List"]')
    assert wishlist_link.is_displayed(), 'Wish List link no es desplegado'
    wishlist_link.click()
    time.sleep(2)

    wl_remove_item_btn : WebElement = driver.find_element(By.XPATH, '//a[@data-original-title = "Remove"]')
    assert wl_remove_item_btn.is_displayed(), 'Remove item button no es mostrado'
    time.sleep(1)

def logout():

    #Logout from account
    my_acct_menu_opt : WebElement = driver.find_element(By.XPATH,'//li//a[@title = "My Account"]')
    assert my_acct_menu_opt.is_displayed(), 'No se encuentra la opcion de My Account'
    my_acct_menu_opt.click()
    time.sleep(2)
    logout_menu_opt : WebElement = driver.find_element(By.XPATH,'//li//a[text() = "Logout"]')
    assert logout_menu_opt.is_displayed(), 'No se encuentra la opcion de Logout'
    logout_menu_opt.click()
    time.sleep(1)


@pytest.mark.qaminds
def test_add_tablet_to_cart():
    product = 'Samsung Galaxy Tab 10.1'
    price = '$241.99'
    driver.maximize_window()
    

    login()

    #**************************************************************

    #Click en menu tablets
    tablets_menu : WebElement = driver.find_element(By.XPATH,'//div[@class = "collapse navbar-collapse navbar-ex1-collapse"]//a[text()="Tablets"]')
    assert tablets_menu.is_displayed(), 'No se encuentra la opción de Tablets en el menu'
    tablets_menu.click()
    time.sleep(2)

    #click en producto desplegado
    product_caption : WebElement = driver.find_element(By.XPATH,f'//h4//a[text() = "{product}"]')
    assert product_caption.is_displayed(), f'No se despliega el producto "{product}"'
    product_caption.click()
    time.sleep(2)

    #verificar que estamos en la pagina del producto verificado
    prod_page_caption: WebElement = driver.find_element(By.XPATH,f'//div//h1[text() = "{product}"]')
    assert prod_page_caption.is_displayed(), f'No se despliega la pagina para el producto "{product}"'
    
    #verificar precio es correcto
    price_caption: WebElement = driver.find_element(By.XPATH,f'//li//h2[text() = "{price}"]')
    assert price_caption.is_displayed(), f'No se despliega el precio para {product} =  "{price}"'
    time.sleep(2)

    #agregar producto en wishlist - click en boton
    add_to_wishlist_button: WebElement = driver.find_element(By.XPATH,'//button[@data-original-title = "Add to Wish List"]')
    assert add_to_wishlist_button.is_displayed(), f'No se despliega el boton de agregar al Wishlist'
    add_to_wishlist_button.click()
    time.sleep(2)

    #agregar producto al carrito
    add_to_cart_button: WebElement = driver.find_element(By.XPATH,'//button[@id = "button-cart"]')
    assert add_to_cart_button.is_displayed(), f'No se despliega el boton de agregar al carrito'
    add_to_cart_button.click()
    time.sleep(3)

    #verificar producto se encuentra en el carrito desde el boton de la esquina superior derecha
    shopping_cart_button: WebElement = driver.find_element(By.XPATH,f'//span[@id = "cart-total" and contains(text(),"{price}")]')
    assert shopping_cart_button.is_displayed(), 'Shopping Cart button no es desplegado con valor del articulo'
    time.sleep(1)    
    
    #verificar producto se agrego al wishlist
    wishlist_link : WebElement = driver.find_element(By.XPATH, '//li//a[text() = "Wish List"]')
    assert wishlist_link.is_displayed(), 'Wish List link no es desplegado'
    wishlist_link.click()
    time.sleep(2)

    wl_product_caption: WebElement = driver.find_element(By.XPATH,f'//td//a[contains(text(),"{product}")]')
    assert wl_product_caption.is_displayed(), 'Producto no fue agregado al Wish List'
    time.sleep(2)

    #**********************************************************************************************

    limpiar_carrito()
    limpiar_wishlist()
    logout()
    



def teardown():
    driver.quit()