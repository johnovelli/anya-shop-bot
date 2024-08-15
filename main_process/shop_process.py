import time
import pyautogui

from actions.open_weapons import openWeapons
from trade_process.armor_process import armorProcess
from capture.get_target import getTargetValues, getTargetBorder_Center
from capture.game_center import moveToGameWindowCenter


def shopProcess(game_window):

    opened_shop_values = getTargetValues(game_window, 'imgs/shop/anya_shop.jpg')
    in_tp_values = getTargetValues(game_window, 'imgs/portal/in_town_tp.jpg')

    if opened_shop_values['max_val'] >= 0.75:

        armorProcess(game_window)
        openWeapons(game_window)
        # clawProcess(game_window)

        if in_tp_values['max_val'] >= 0.75:
            in_tp_center = (
                getTargetBorder_Center(game_window, in_tp_values['top_left'], in_tp_values['bot_right'], (128, 55, 30))
             )
            moveToGameWindowCenter("Diablo II: Resurrected", in_tp_center)
            pyautogui.click()
            time.sleep(3)
            return False

    return True
