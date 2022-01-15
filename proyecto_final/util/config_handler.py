
import json
import proyecto_final.util.constants as constants


class ConfigHadler():
    __browser = None
    __chrome_driver = None
    __firefox_driver = None
    __url = None
    __incognite_mode = False
    __headless_enabled = False
    __headless_height = None
    __headless_weight = None
    __explicit_wait_small = 0
    __explicit_wait_medium = 0
    __explicit_wait_large = 0
    __evidence_path = None
    __data_set_path = None
    __firefox_opt_location = None

    

    def __init__(self) -> None:
       self.__load_general_config()
     
       
    def __load_general_config(self):
        with open(constants.DIR_FILE_CONFIG) as json_file:
            config = json.load(json_file)
            self.__browser = config["browser"]
            self.__url = config["url"]
            self.__incognite_mode = config["incognite_mode"]
            self.__headless_enabled = config["headless"]["enabled"]
            self.__headless_height = config["headless"]["resolution"]["height"]
            self.__headless_weight = config["headless"]["resolution"]["width"]
            self.__explicit_wait_small = config["explicit_wait"]["small"]
            self.__evidence_path = config["evidence"]["path"]
            self.__data_set_path = config["data_set"]["path"]
            self.__chrome_driver = config["chrome"]["driver"]
            self.__firefox_driver = config["firefox"]["driver"]
            self.__firefox_opt_location = config["firefox"]["option_location"]
            
         

    def get_browser(self):
        return self.__browser

    def get_chrome_driver(self):
        return self.__chrome_driver
    
    def get_firefox_driver(self):
        return self.__firefox_driver
    
    def get_firefox_opt_location(self):
        return self.__firefox_opt_location

    def get_url(self):
        return self.__url

    def get_incognite_mode(self):
        return self.__incognite_mode

    def get_headless_enabled(self):
        return self.__headless_enabled

    def get_headless_height(self):
        return self.__headless_height

    def get_headless_weight(self):
        return self.__headless_weight

    def get_explicit_wait_small(self):
        return self.__explicit_wait_small

    def get_evidence_path(self):
        return self.__evidence_path

    def get_data_path(self):
        return self.__data_set_path
    

