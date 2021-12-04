import json

CONFIG_FILE = './clase_09/config.json'

browser_name = None
driver_path = None
incognito = False
headless_mode = False
headless_resolution = None
page_load = 0
implicit_wait_mode = False
implicit_wait_time = 0
url_app = None
explicit_wait_short = 0
explicit_wait_medium = 0
explicit_wait_large = 0

def load_config():
    global browser_name, driver_path, incognito, headless_mode, headless_resolution, page_load, implicit_wait_mode, implicit_wait_time, url_app, explicit_wait_large, explicit_wait_medium, explicit_wait_short
    try:
        with open(CONFIG_FILE,'r') as file:
            data = json.load(file)
            browser_name = data['browser_name']
            driver_path = data["driver_path"]
            incognito = data["incognito"]
            headless_mode = data["headless"]["enabled"]
            headless_resolution = data["headless"]["resolution"]
            page_load = data["page_load"]
            implicit_wait_mode = data["implicit_wait"]["enabled"]
            implicit_wait_time = data["implicit_wait"]["time"]
            url_app = data["url_app"]
            explicit_wait_short = data["explicit_wait"]["short"]
            explicit_wait_medium = data["explicit_wait"]["medium"]
            explicit_wait_large = data["explicit_wait"]["large"]
    except Exception as e:
        raise KeyError(f'Error en la obtencion de parametros: {e}')

def get_browser_name():
    return browser_name

def get_driver_path():
    return driver_path

def get_incognito_mode():
    return incognito

def get_headless_mode():
    return headless_mode

def get_headless_resolution():
    return headless_resolution

def get_page_load():
    return page_load

def get_implicit_wait_mode():
    return implicit_wait_mode

def get_implicit_wait_time():
    return implicit_wait_time

def get_url_app():
    return url_app

def get_explicit_wait_short():
    return explicit_wait_short

def get_explicit_wait_medium():
    return explicit_wait_medium

def get_explicit_wait_large():
    return explicit_wait_large