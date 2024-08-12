import time
import keyboard
import pyautogui
from find_target import getTargetValues, getTargetBorder_Center
from game_center import moveToGameWindowCenter


def processAnya(game_window):

    anya_best_match = {'max_val': 0, 'top_left': (0, 0), 'bot_right': (0, 0)}
    anya_imgs = ['imgs/anya/anya1.jpg', 'imgs/anya/anya2.jpg', 'imgs/anya/anya3.jpg', 'imgs/anya/anya4.jpg', 'imgs/anya/anya5.jpg']

    for anya_img in anya_imgs:
        anya_values = getTargetValues(game_window, anya_img)
        if anya_values['max_val'] > anya_best_match['max_val']:
            anya_best_match = anya_values

    if anya_best_match['max_val'] >= 0.55:
        anya_center = (
            getTargetBorder_Center(game_window, anya_best_match['top_left'], anya_best_match['bot_right'], (28, 255, 80))
        )
        time.sleep(1)
        moveToGameWindowCenter("Diablo II: Resurrected", anya_center)
