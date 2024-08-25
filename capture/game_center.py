import pygetwindow as gw
import pyautogui


def moveToGameWindowCenter(game_window, center):
    # Get the game window with the specified title
    game_window = gw.getWindowsWithTitle(game_window)[0]

    # Calculate the absolute position to move the cursor based on the game window's position and the target center
    absolute_x = game_window.left + center[0]
    absolute_y = game_window.top + center[1]

    # Move the cursor to the calculated position
    pyautogui.moveTo(absolute_x, absolute_y)