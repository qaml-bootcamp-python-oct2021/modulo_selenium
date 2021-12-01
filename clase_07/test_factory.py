import factory_driver

driver = None

def setup():
    global driver
    driver = factory_driver.get_driver('firefox')
    driver.get('https://qamindslab.com/#/')

def test_driver():
    assert 'QA Minds Lab' == driver.title

def teardown():
    driver.quit()