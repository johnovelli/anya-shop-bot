import pytesseract


def imgToString(capture_attributes):
    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    attributes_img = capture_attributes()
    attributes = pytesseract.image_to_string(attributes_img)
    lines = attributes.splitlines()
    return lines, attributes_img
