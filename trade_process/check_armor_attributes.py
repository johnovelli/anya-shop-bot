from capture.capture_attributes import capture_armor_attributes, att_screenshot
from capture.img_to_string import imgToString
from config.get_config_values import get_params
from trade_process.item_dictionary import socketed_lines, life_lines


def checkArmorAttributes():

    life_in_range = False
    four_socketed = False

    min_life = int(get_params()['min_life'])
    min_sockets = int(get_params()['min_sockets'])

    life_range = list(range(min_life, 101))
    sockets_range = list(range(min_sockets, 5))

    lines, attributes_img = imgToString(capture_armor_attributes)

    for line in lines:
        line = line.lower()

        is_life_range = (any(str(num) in line for num in life_range))
        if any(life in line for life in life_lines) and is_life_range:
            print('Life in range:' + line)
            att_screenshot('armor', attributes_img)
            life_in_range = True

        is_sockets_range = (any(str(num) in line for num in sockets_range))
        if (any(socketed in line for socketed in socketed_lines)
                and is_sockets_range):
            print('Socketed in range:' + line)
            att_screenshot('armor', attributes_img)
            four_socketed = True

    if life_in_range and four_socketed:
        print('50x jah!')
        return True

    return False
