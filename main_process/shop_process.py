from actions.leave_town import leaveTown
from actions.open_weapons import openWeapons
from trade_process.armor_process import armorProcess
from capture.get_target import getTargetValues
from trade_process.claw_process import clawProcess


def shopProcess(game_window):

    opened_shop_values = getTargetValues(game_window, 'imgs/shop/anya_shop.jpg')
    if opened_shop_values['max_val'] >= 0.75:

        armorProcess(game_window)
        openWeapons(game_window)
        clawProcess()

        return leaveTown(game_window)

    return True
