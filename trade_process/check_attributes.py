import pytesseract
import cv2 as cv

from trade_process.capture_attributes import capture_attributes


def checkAttributes():
    numbers_range = list(range(60, 101))
    life_in_range = False
    four_socketed = False

    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    attributes_img = capture_attributes()
    attributes = pytesseract.image_to_string(attributes_img)
    lines = attributes.splitlines()
    for line in lines:
        line = line.lower()
        life_range = (any(str(num) in line for num in numbers_range))
        if 'lire' in line or 'life' in line:
            print('Armor life:' + line)
        if 'secketed' in line or 'socketed' in line:
            print('Armor socketed:' + line)
        if ('lire' in line or 'life' in line) and life_range:
            life_in_range = True
            print('Life in range:' + line)
        if ('secketed' in line or 'socketed' in line) and '4' in line:
            four_socketed = True
            print('4 socketed:' + line)

    if life_in_range and four_socketed:
        print('i`m rich!')
        return True

    return False



