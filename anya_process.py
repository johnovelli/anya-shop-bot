import time
import pyautogui
from find_target import getTargetValues, getTargetBorder_Center
from capture_window.game_center import moveToGameWindowCenter
from back_to_town import backToTown
from start_trade import startTrade


def processAnya(game_window):

    backToTown(game_window)

    if startTrade(game_window):
        return True

    anya_best_match = {'max_val': 0, 'top_left': (0, 0), 'bot_right': (0, 0)}
    anya_imgs = ['imgs/anya/anya1.jpg', 'imgs/anya/anya2.jpg', 'imgs/anya/anya3.jpg', 'imgs/anya/anya4.jpg', 'imgs/anya/anya5.jpg', 'imgs/anya/anya6.jpg']

    for anya_img in anya_imgs:
        anya_values = getTargetValues(game_window, anya_img)
        if anya_values['max_val'] > anya_best_match['max_val']:
            anya_best_match = anya_values

    if anya_best_match['max_val'] >= 0.55:
        anya_center = (
            getTargetBorder_Center(game_window, anya_best_match['top_left'], anya_best_match['bot_right'], (28, 255, 80))
        )
        moveToGameWindowCenter("Diablo II: Resurrected", anya_center)
        pyautogui.click()
        time.sleep(2)

    return False
