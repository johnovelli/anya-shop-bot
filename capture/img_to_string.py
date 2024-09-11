import os
import pytesseract

from config.get_config_values import get_tesseract_path


def imgToString(capture_attributes):
    # Set the Tesseract executable path based on the operating system
    if os.name == 'nt':
        pytesseract.pytesseract.tesseract_cmd = os.path.join(get_tesseract_path(), 'tesseract.exe')
    else:
        pytesseract.pytesseract.tesseract_cmd = os.path.join(get_tesseract_path(), 'tesseract')

    # Capture the image attributes and convert the image to a string using Tesseract
    attributes_img = capture_attributes()
    attributes = pytesseract.image_to_string(attributes_img)

    # Split the resulting string into lines
    lines = attributes.splitlines()

    # Return the extracted text lines and the image itself
    return lines, attributes_img
