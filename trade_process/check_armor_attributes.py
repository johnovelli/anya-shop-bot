import pytesseract

from datetime import datetime
from capture.capture_attributes import capture_attributes


def checkArmorAttributes():
    numbers_range = list(range(40, 101))
    life_in_range = False
    four_socketed = False

    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    attributes_img = capture_attributes()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    attributes_img.save(f'imgs/logs/armor/{timestamp}.jpg')
    attributes = pytesseract.image_to_string(attributes_img)
    lines = attributes.splitlines()

    for line in lines:
        line = line.lower()
        life_range = (any(str(num) in line for num in numbers_range))
        if 'lire' in line or 'life' in line:
            print('Armor life:' + line)
        if 'secketed' in line or 'socketed' in line or '(' in line:
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



