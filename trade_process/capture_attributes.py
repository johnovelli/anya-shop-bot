import pyautogui


def capture_attributes():

    mouse_x, mouse_y = pyautogui.position()
    left = mouse_x - 150 // 2
    top = mouse_y - 375 // 2

    screenshot = pyautogui.screenshot(region=(left, top, 300, 450))
    screenshot.save('imgs/logs')
    return screenshot
