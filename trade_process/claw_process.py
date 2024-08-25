import time
import pyautogui

from trade_process.check_claw_attributes import checkClawAttributes


#  Processes armors in the game window to determine if they should be bought.
def clawProcess():
    # List of relative locations to move the cursor for checking claws
    claw_locs = [(-125, 65), (0, 115), (0, 115), (40, -220), (0, 115), (0, 115)]

    # Iterate over each location
    for claw_loc in claw_locs:
        # Move the cursor relative to the current position
        pyautogui.moveRel(claw_loc)
        time.sleep(0.5)  # Wait for half a second to allow any visual changes to settle

        # Check if the claw at the current location meets the attributes criteria
        if checkClawAttributes():
            print('')
            print('i have to buy :D')  # Message indicating that the claw should be bought
            pyautogui.click(button='right')  # Click the right mouse button, buying te item


# For attribute test:
# (790, -15)
# Old logic using color filter (not working xD):
# from capture.color_filter import filterYellowColor
# from capture.get_target import getTargetBorder_Center, getItemValues
# from capture.game_center import moveToGameWindowCenter
    # claw_values_list = getItemValues(game_window, 'imgs/shop/claws/greater_talon.jpg', 0.3, filterYellowColor)
    # print(claw_values_list)
    # for claw_values in claw_values_list:
    #     claw_center = (
    #         getTargetBorder_Center(game_window, claw_values['top_left'], claw_values['bot_right'], (255, 255, 0))
    #     )
    #     moveToGameWindowCenter("Diablo II: Resurrected", claw_center)
    #     time.sleep(2)