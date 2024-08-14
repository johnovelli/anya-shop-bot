import pygetwindow as gw
import pyautogui


def moveToGameWindowCenter(game_window, center):
    game_window = gw.getWindowsWithTitle(game_window)[0]
    absolute_x = game_window.left + center[0]
    absolute_y = game_window.top + center[1]
    pyautogui.moveTo(absolute_x, absolute_y)
