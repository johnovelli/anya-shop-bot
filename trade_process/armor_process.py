import time
import pyautogui

from capture.color_filter import filterRedColor
from capture.get_target import getItemValues, getTargetBorder_Center
from capture.game_center import moveToGameWindowCenter
from trade_process.check_armor_attributes import checkArmorAttributes


def armorProcess(game_window):

    armor_imgs = ['imgs/shop/armors/light_plate.jpg', 'imgs/shop/armors/ancient_armor.jpg', 'imgs/shop/armors/ancient_armor2.jpg']
    for armor_img in armor_imgs:
        armor_values_list = getItemValues(game_window, armor_img, 0.8, filterRedColor)

        for armor_values in armor_values_list:
            armor_center = (
                getTargetBorder_Center(game_window, armor_values['top_left'], armor_values['bot_right'], (255, 255, 0))
            )
            moveToGameWindowCenter("Diablo II: Resurrected", armor_center)
            time.sleep(0.5)

            if checkArmorAttributes():
                print('')
                print('i have to buy :D')
                pyautogui.click(button='right')
