import pyautogui


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
    screenshot = pyautogui.screenshot(region=(left, top, 430, 550))
    return screenshot
