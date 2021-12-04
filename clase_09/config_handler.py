
import json
browser = None
driver = None
url = None
incognite_mode = False
headless_enabled = False
headless_height = None
headless_weight = None
explicit_wait_small = 0
explicit_wait_medium = 0
explicit_wait_large = 0


def load_config():
    global browser, driver, url, incognite_mode, headless_enabled, headless_height, headless_weight, explicit_wait_small

    with open('./clase_09/config.json') as json_file:
        config = json.load(json_file)
        browser = config["browser"]
        driver = config["driver"]
        url = config["url"]
        incognite_mode = config["incognite_mode"]
        headless_enabled = config["headless"]["enabled"]
        headless_height = config["headless"]["resolution"]["height"]
        headless_weight = config["headless"]["resolution"]["width"]
        explicit_wait_small = config["explicit_wait"]["small"]


def get_browser():
    return browser


def get_driver():
    return driver


def get_url():
    return url


def get_incognite_mode():
    return incognite_mode


def get_headless_enabled():
    return headless_enabled


def get_headless_height():
    return headless_height


def get_headless_weight():
    return headless_weight

def get_explicit_wait_small():
    return explicit_wait_small  
