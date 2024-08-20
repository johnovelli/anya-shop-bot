import os
import pytesseract

from config.get_config_values import get_tesseract_path


def imgToString(capture_attributes):

    if os.name == 'nt':
        pytesseract.pytesseract.tesseract_cmd = os.path.join(get_tesseract_path(), 'tesseract.exe')
    else:
        pytesseract.pytesseract.tesseract_cmd = os.path.join(get_tesseract_path(), 'tesseract')

    attributes_img = capture_attributes()
    attributes = pytesseract.image_to_string(attributes_img)
    lines = attributes.splitlines()
    return lines, attributes_img
