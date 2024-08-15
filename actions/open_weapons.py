import time
import pyautogui

from capture.game_center import moveToGameWindowCenter
from capture.get_target import getTargetValues, getTargetBorder_Center


def openWeapons(game_window):
    weapons_values = getTargetValues(game_window, 'imgs/shop/weapons.jpg')
    if weapons_values['max_val'] >= 0.5:
        weapons_center = (
            getTargetBorder_Center(game_window, weapons_values['top_left'], weapons_values['bot_right'], (128, 55, 30))
        )
        moveToGameWindowCenter("Diablo II: Resurrected", weapons_center)
        pyautogui.click()
        time.sleep(0.5)
