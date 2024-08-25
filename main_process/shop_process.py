from actions.leave_town import leaveTown
from actions.open_weapons import openWeapons
from trade_process.armor_process import armorProcess
from capture.get_target import getTargetValues
from trade_process.claw_process import clawProcess


#  Handles the shop process
def shopProcess(game_window):

    # Get the values of the shop image to check if the shop is open
    opened_shop_values = getTargetValues(game_window, 'imgs/shop/anya_shop.jpg')

    # Check if the shop image matches with a confidence threshold
    if opened_shop_values['max_val'] >= 0.75:
        # Process armor items in the shop
        armorProcess(game_window)
        # Open the weapons section of the shop
        openWeapons(game_window)
        # Process claw items in the shop
        clawProcess()

        # Leave the town after completing the shop process
        return leaveTown(game_window)

    return True