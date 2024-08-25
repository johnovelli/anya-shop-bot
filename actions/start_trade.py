import pyautogui

from capture.game_center import moveToGameWindowCenter
from capture.get_target import getTarget_Center, getTargetValues


# Starts the trade process by finding and clicking on the trade interface.
def startTrade(game_window):

    trade_best_match = {'max_val': 0, 'top_left': (0, 0), 'bot_right': (0, 0)}
    trade_imgs = ['imgs/shop/trade1.jpg', 'imgs/shop/trade2.jpg']

    # Iterate over each trade image to find the best match
    for trade_img in trade_imgs:
        trade_values = getTargetValues(game_window, trade_img)
        if trade_values['max_val'] > trade_best_match['max_val']:
            trade_best_match = trade_values

    # Check if the best match image meets the confidence threshold
    if trade_best_match['max_val'] >= 0.55:
        # Get the center position of the trade interface
        trade_center = (
            getTarget_Center(game_window, trade_best_match['top_left'], trade_best_match['bot_right'], (128, 255, 180))
        )
        # Move to the center of the trade interface and click to start trading
        moveToGameWindowCenter("Diablo II: Resurrected", trade_center)
        pyautogui.click()
        return True

    return False