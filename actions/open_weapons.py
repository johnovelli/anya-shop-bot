import time
import pyautogui

from capture.game_center import moveToGameWindowCenter
from capture.get_target import getTargetValues, getTarget_Center


# Opens the weapons section of the shop.
def openWeapons(game_window):
    # Get the values of the weapons image to check if the weapons section is visible
    weapons_values = getTargetValues(game_window, 'imgs/shop/weapons.jpg')

    # Check if the weapons image matches with a confidence threshold
    if weapons_values['max_val'] >= 0.4:
        # Get the center position of the weapons section
        weapons_center = (
            getTarget_Center(game_window, weapons_values['top_left'], weapons_values['bot_right'], (128, 55, 30))
        )
        # Move to the center of the weapons section and click to open it
        moveToGameWindowCenter("Diablo II: Resurrected", weapons_center)
        pyautogui.click()
        time.sleep(0.5)  # Wait for the action to complete
