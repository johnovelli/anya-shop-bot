import time
import pyautogui

from trade_process.check_attributes import checkAttributes
from capture.find_target import getTargetValues, getItemValues, getTargetBorder_Center
from capture.game_center import moveToGameWindowCenter


def shopProcess(game_window):

    opened_shop_values = getTargetValues(game_window, 'imgs/shop/anya_shop.jpg')
    in_tp_values = getTargetValues(game_window, 'imgs/portal/in_town_tp.jpg')

    if opened_shop_values['max_val'] >= 0.75:
        time.sleep(1)
        armor_imgs = ['imgs/shop/armors/light_plate.jpg', 'imgs/shop/armors/ancient_armor.jpg', 'imgs/shop/armors/ancient_armo2.jpg']
        for armor_img in armor_imgs:
            armor_values = getItemValues(game_window, armor_img)
            if armor_values['max_val'] >= 0.8:
                armor_center = (
                    getTargetBorder_Center(game_window, armor_values['top_left'], armor_values['bot_right'], (255, 255, 0))
                )
                moveToGameWindowCenter("Diablo II: Resurrected", armor_center)
                time.sleep(2)

                if checkAttributes():
                    print('i have to buy :D')
                    pyautogui.click(button='right')

        if in_tp_values['max_val'] >= 0.75:
            in_tp_center = (
                getTargetBorder_Center(game_window, in_tp_values['top_left'], in_tp_values['bot_right'], (128, 55, 30))
             )
            moveToGameWindowCenter("Diablo II: Resurrected", in_tp_center)
            pyautogui.click()
            time.sleep(3)
            return False

    return True
