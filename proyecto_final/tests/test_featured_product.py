import pytest
from proyecto_final.pages.home_page import HomePage
from proyecto_final.drivers import factory_driver
from proyecto_final.pages.product_page import ProductPage
from proyecto_final.pages.shopping_page import ShoppingPage
from proyecto_final.utils import data_handler


driver = None

def setup():
    global driver
    driver = factory_driver.get_driver()

@pytest.mark.parametrize('featured_product,quantity,color',[(data_handler.get_data('./proyecto_final/dataset/featured_product.csv'))])
def test_featured_product(featured_product,quantity,color):
    home = HomePage(driver)
    home.select_feature_product(featured_product)
    product = ProductPage(driver)
    product.verify_product_page(featured_product)
    product.select_available_option(color)
    product.write_quantity_value(quantity)
    product.click_button_cart()
    product.verify_menssage_alert()
    product.take_screenshot()
    product.click_shopping_cart_link()
    shopping = ShoppingPage(driver)
    shopping.verify_shopping_page_with_product(featured_product)
    home.click_logo()
    home.verify_home_page()


def teardown():
    HomePage(driver).close_browser()