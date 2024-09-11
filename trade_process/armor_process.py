import time
import pyautogui

from capture.color_filter import filterRedColor
from capture.get_target import getItemValues, getTarget_Center
from capture.game_center import moveToGameWindowCenter
from trade_process.check_armor_attributes import checkArmorAttributes


#  Processes armors in the game window to determine if they should be bought.
def armorProcess(game_window):

    # List of armor images to search for in the game window
    armor_imgs = ['imgs/shop/armors/light_plate.jpg', 'imgs/shop/armors/ancient_armor.jpg', 'imgs/shop/armors/ancient_armor2.jpg']

    # Iterate over each armor image
    for armor_img in armor_imgs:
        # Get item values for the armor image
        armor_values_list = getItemValues(game_window, armor_img, 0.8, filterRedColor)

        # Iterate over the armor values found
        for armor_values in armor_values_list:
            # Get the center of the armor's target for checking
            armor_center = (
                getTarget_Center(game_window, armor_values['top_left'], armor_values['bot_right'], (255, 255, 0))
            )
            # Move the cursor to the center of the game window
            moveToGameWindowCenter("Diablo II: Resurrected", armor_center)
            time.sleep(0.5)

            # Check if the armor meets the criteria for purchase
            if checkArmorAttributes():
                print('')
                print('i have to buy :D')  # Message indicating that the armor should be bought
                pyautogui.click(button='right')  # Click the right mouse button, buying te item
