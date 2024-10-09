import time
import pyautogui

from capture.game_center import moveToGameWindowCenter
from capture.get_target import getTargetValues, getTarget_Center


# Moves player out of town by using the red portal.
def leaveTown(game_window):

    # Get the values of the town portal image to check if the player is at the town portal
    in_tp_values = getTargetValues(game_window, 'imgs/portal/in_town_tp.jpg')

    # Check if the town portal image matches with a confidence threshold
    if in_tp_values['max_val'] >= 0.35:
        # Get the center position of the town portal
        in_tp_center = (
            getTarget_Center(game_window, in_tp_values['top_left'], in_tp_values['bot_right'], (128, 55, 30))
        )
        # Move to the center of the town portal and click to use it
        moveToGameWindowCenter("Diablo II: Resurrected", in_tp_center)
        pyautogui.click()
        time.sleep(3)  # Wait for the action to complete
        return False
