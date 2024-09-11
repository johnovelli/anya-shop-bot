import configparser

config_file = 'config.ini'


def get_tesseract_path():
    # Load the configuration file and return the Tesseract executable path
    config = configparser.ConfigParser()
    config.read(config_file)
    return config['tesseract']['pytesseract_path']


def get_params():
    # Load the configuration file and return the parameters section
    config = configparser.ConfigParser()
    config.read(config_file)
    return config['params']
