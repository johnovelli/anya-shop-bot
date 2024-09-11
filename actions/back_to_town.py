import time
import pyautogui

from capture.get_target import getTargetValues, getTarget_Center
from capture.game_center import moveToGameWindowCenter


# Returns the player to town by using the red portal.
def backToTown(game_window):

    # Get the values of the image to check if the player is in the out of town.
    out_area_values = getTargetValues(game_window, 'imgs/portal/out_town_area.jpg')

    # Check if the player is in the out-of-town area with a confidence threshold
    if out_area_values['max_val'] >= 0.85:
        # Get the values of the town portal image to check if the town portal is present
        out_tp_values = getTargetValues(game_window, 'imgs/portal/out_town_tp.jpg')

        # Check if the town portal image matches with a confidence threshold
        if out_tp_values['max_val'] >= 0.65:
            # Get the center position of the town portal
            out_tp_center = (
                getTarget_Center(game_window, out_tp_values['top_left'], out_tp_values['bot_right'], (128, 155, 60))
            )
            time.sleep(1.5)  # Wait for a short period before clicking
            # Move to the center of the town portal and click to use it
            moveToGameWindowCenter("Diablo II: Resurrected", out_tp_center)
            pyautogui.click()
            time.sleep(2)  # Wait for the teleportation to complete
