
import logging
from proyecto_final.util.config_handler import ConfigHadler

config: ConfigHadler = None


def get_config():
    global config
    if  config == None:
        config = ConfigHadler()
      
    return config




