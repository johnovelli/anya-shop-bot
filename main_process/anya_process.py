import time
import pyautogui
from capture.get_target import getTargetValues, getTarget_Center
from capture.game_center import moveToGameWindowCenter
from actions.back_to_town import backToTown
from actions.start_trade import startTrade


# Process the interaction with Anya in the game
def processAnya(game_window):

    # Move the character back to town
    backToTown(game_window)

    # Start trade with Anya, return True if successful
    if startTrade(game_window):
        return True

    # Best match for Anya's images
    anya_best_match = {'max_val': 0, 'top_left': (0, 0), 'bot_right': (0, 0)}
    # List of images to search for Anya
    anya_imgs = ['imgs/anya/anya1.jpg', 'imgs/anya/anya2.jpg', 'imgs/anya/anya3.jpg', 'imgs/anya/anya4.jpg', 'imgs/anya/anya5.jpg', 'imgs/anya/anya6.jpg']

    # Find the best match for Anya's image in the game window
    for anya_img in anya_imgs:
        anya_values = getTargetValues(game_window, anya_img)
        if anya_values['max_val'] > anya_best_match['max_val']:
            anya_best_match = anya_values

    # If a good match is found, move the cursor to Anya and click
    if anya_best_match['max_val'] >= 0.55:
        anya_center = getTarget_Center(game_window, anya_best_match['top_left'], anya_best_match['bot_right'], (28, 255, 80))
        moveToGameWindowCenter("Diablo II: Resurrected", anya_center)
        pyautogui.click()
        time.sleep(1.25)

    return False