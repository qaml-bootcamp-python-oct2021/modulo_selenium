from proyecto_final.drivers import factory_driver
import time

def test_init ():
    driver = factory_driver.get_driver()
    time.sleep(3)
    driver.quit()
    