from datetime import datetime

from capture.capture_attributes import capture_armor_attributes
from capture.img_to_string import imgToString


def checkArmorAttributes():
    life_in_range = False
    four_socketed = False
    numbers_range = list(range(80, 101))

    lines, attributes_img = imgToString(capture_armor_attributes)
    for line in lines:
        line = line.lower()

        life_range = (any(str(num) in line for num in numbers_range))
        socketed_lines = ['secketed', 'socketed', ')', 'sk', 'ser']

        if any(socketed in line for socketed in socketed_lines):
            print('Armor socketed:' + line)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            attributes_img.save(f'imgs/logs/armor/{timestamp}.jpg')

        if ('lire' in line or 'life' in line) and life_range:
            print('Life in range:' + line)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            attributes_img.save(f'imgs/logs/armor/{timestamp}.jpg')
            life_in_range = True

        if any(socketed in line for socketed in socketed_lines) and '4' in line:
            print('4 socketed:' + line)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            attributes_img.save(f'imgs/logs/armor/{timestamp}.jpg')
            four_socketed = True

        if life_in_range and four_socketed:
            return True

    return False
