import time
import pyautogui
from find_target import getTargetValues, getTargetBorder_Center
from capture_window.game_center import moveToGameWindowCenter


def processShop(game_window):

    in_town_tp = 'imgs/portal/in_town_tp.jpg'

    time.sleep(1)

    in_tp_values = getTargetValues(game_window, in_town_tp)
    if in_tp_values['max_val'] >= 0.75:
        in_tp_center = (
            getTargetBorder_Center(game_window, in_tp_values['top_left'], in_tp_values['bot_right'], (128, 55, 30))
        )
        moveToGameWindowCenter("Diablo II: Resurrected", in_tp_center)
        pyautogui.click()
        time.sleep(5)
        return False

    return True
