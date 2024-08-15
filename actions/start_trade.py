import pyautogui

from capture.game_center import moveToGameWindowCenter
from capture.get_target import getTargetBorder_Center, getTargetValues


def startTrade(game_window):

    trade_best_match = {'max_val': 0, 'top_left': (0, 0), 'bot_right': (0, 0)}
    trade_imgs = ['imgs/shop/trade1.jpg', 'imgs/shop/trade2.jpg']

    for trade_img in trade_imgs:
        trade_values = getTargetValues(game_window, trade_img)
        if trade_values['max_val'] > trade_best_match['max_val']:
            trade_best_match = trade_values

    if trade_best_match['max_val'] >= 0.55:
        trade_center = (
            getTargetBorder_Center(game_window, trade_best_match['top_left'], trade_best_match['bot_right'], (128, 255, 180))
        )
        moveToGameWindowCenter("Diablo II: Resurrected", trade_center)
        pyautogui.click()
        return True

    return False
