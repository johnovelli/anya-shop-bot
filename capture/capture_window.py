import mss
import pygetwindow as gw
import cv2 as cv
import numpy as np


def capture_game_window(game_title):
    # Get the game window with the specified title
    game_window = gw.getWindowsWithTitle(game_title)[0]

    if not game_window:
        # Raise an error if the game window is not found
        raise ValueError(f"Window with title '{game_title}' not found.")

    # Define the area of the game window for capturing
    game_area = (game_window.left, game_window.top, game_window.right, game_window.bottom)

    # Capture the game window using mss
    with mss.mss() as sct:
        game_window_imgs = sct.grab(game_area)

        # Convert the captured image to BGR format for OpenCV
        game_window = cv.cvtColor(np.array(game_window_imgs), cv.COLOR_BGRA2BGR)

    return game_window
