import pyautogui

from datetime import datetime


def capture_armor_attributes():
    # Get the current mouse position
    mouse_x, mouse_y = pyautogui.position()

    # Calculate the top-left corner of the screenshot region based on mouse position
    left = mouse_x - 150 // 2
    top = mouse_y - 375 // 2

    # Capture a screenshot of the specified region around the mouse cursor
    screenshot = pyautogui.screenshot(region=(left, top, 320, 450))

    return screenshot


def capture_claw_attributes():
    # Get the current mouse position
    mouse_x, mouse_y = pyautogui.position()

    # Calculate the top-left corner of the screenshot region based on mouse position
    left = mouse_x - 150 // 2
    top = mouse_y - 400 // 2

    # Capture a screenshot of the specified region around the mouse cursor
    screenshot = pyautogui.screenshot(region=(left, top, 430, 580))

    return screenshot


def att_screenshot(folder, attributes_img):
    # Create a timestamp for the screenshot file name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Save the screenshot image in the specified folder with the timestamped filename
    attributes_img.save(f'logs/{folder}/{timestamp}.jpg')
