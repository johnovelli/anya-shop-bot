import pyautogui

from datetime import datetime


def capture_armor_attributes():
    mouse_x, mouse_y = pyautogui.position()
    left = mouse_x - 150 // 2
    top = mouse_y - 375 // 2
    screenshot = pyautogui.screenshot(region=(left, top, 320, 450))
    return screenshot


def capture_claw_attributes():
    mouse_x, mouse_y = pyautogui.position()
    left = mouse_x - 150 // 2
    top = mouse_y - 400 // 2
    screenshot = pyautogui.screenshot(region=(left, top, 430, 580))
    return screenshot


def att_screenshot(folder, attributes_img):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    attributes_img.save(f'logs/{folder}/{timestamp}.jpg')