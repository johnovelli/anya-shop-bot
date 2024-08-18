import configparser

config_file = 'config.ini'


def get_tesseract_path():

    config = configparser.ConfigParser()
    config.read(config_file)
    return config['tesseract']['pytesseract_path']


def get_params():

    config = configparser.ConfigParser()
    config.read(config_file)
    return config['params']
