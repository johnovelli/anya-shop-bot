import time
import pyautogui

from capture.get_target import getTargetValues, getTargetBorder_Center
from capture.game_center import moveToGameWindowCenter


def backToTown(game_window):

    out_area_values = getTargetValues(game_window, 'imgs/portal/out_town_area.jpg')

    if out_area_values['max_val'] >= 0.88:
        out_tp_values = getTargetValues(game_window, 'imgs/portal/out_town_tp.jpg')
        if out_tp_values['max_val'] >= 0.65:
            out_tp_center = (
                getTargetBorder_Center(game_window, out_tp_values['top_left'], out_tp_values['bot_right'], (128, 155, 60))
            )
            time.sleep(1.5)
            moveToGameWindowCenter("Diablo II: Resurrected", out_tp_center)
            pyautogui.click()
            time.sleep(2)
