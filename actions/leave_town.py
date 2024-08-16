import time
import pyautogui

from capture.game_center import moveToGameWindowCenter
from capture.get_target import getTargetValues, getTargetBorder_Center


def leaveTown(game_window):
    in_tp_values = getTargetValues(game_window, 'imgs/portal/in_town_tp.jpg')

    if in_tp_values['max_val'] >= 0.75:
        in_tp_center = (
            getTargetBorder_Center(game_window, in_tp_values['top_left'], in_tp_values['bot_right'], (128, 55, 30))
        )
        moveToGameWindowCenter("Diablo II: Resurrected", in_tp_center)
        pyautogui.click()
        time.sleep(3)
        return False
