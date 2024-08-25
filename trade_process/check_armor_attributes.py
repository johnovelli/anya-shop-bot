from capture.capture_attributes import capture_armor_attributes, att_screenshot
from capture.img_to_string import imgToString
from config.get_config_values import get_params
from trade_process.item_dictionary import socketed_lines, life_lines


#  Checks if the armor attributes meet the criteria for purchase.
def checkArmorAttributes():

    life_in_range = False
    four_socketed = False

    # Get minimum life and socket parameters from configuration
    min_life = int(get_params()['min_life'])
    min_sockets = int(get_params()['min_sockets'])

    # Define the ranges for life and sockets
    life_range = list(range(min_life, 101))
    sockets_range = list(range(min_sockets, 5))

    # Convert armor attributes image to a list of text lines
    lines, attributes_img = imgToString(capture_armor_attributes)

    # Iterate over each line of attributes
    for line in lines:
        line = line.lower()  # Convert the line to lowercase

        # Check if life is within the desired range
        is_life_range = (any(str(num) in line for num in life_range))
        if any(life in line for life in life_lines) and is_life_range:
            print("")
            print('Life in range:' + line)  # Message indicating that life is within the range
            att_screenshot('armor', attributes_img)  # Capture a screenshot of the attributes
            life_in_range = True

        # Check if the number of sockets is within the desired range
        is_sockets_range = (any(str(num) in line for num in sockets_range))
        if (any(socketed in line for socketed in socketed_lines)
                and is_sockets_range):
            print("")
            print('Socketed in range:' + line)  # Message indicating that the number of sockets is within the range
            att_screenshot('armor', attributes_img)  # Capture a screenshot of the attributes
            four_socketed = True

    # Return True if both criteria (life and sockets) are met
    if life_in_range and four_socketed:
        print('')
        print('50x jah!')
        return True

    return False