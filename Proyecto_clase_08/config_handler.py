import json

CONFIG_FILE = './Proyecto_clase_08/config.json'

browser_name = None
driver_path = None
incognito = False
headless_mode = False
headless_resolution = None
page_load = 0
implicit_wait_mode = False
implicit_wait_time = 0
url_app = None

def load_config():
    global browser_name, driver_path, incognito, headless_mode, headless_resolution, page_load, implicit_wait_mode, implicit_wait_time,url_app
    try:
        with open(CONFIG_FILE,'r') as file:
            data = json.load(file)
            browser_name = data['browser_name']
            driver_path = data['driver_path']
            incognito = data['incognito']
            headless_mode = data['headless']['enabled']
            headless_resolution = data['headless']['resolution']
            page_load = data['page_load']
            implicit_wait_mode = data['implicit_wait']['enabled']
            implicit_wait_time = data['implicit_wait']['time']
            url_app = data['url_app']
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