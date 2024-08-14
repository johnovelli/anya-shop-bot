import cv2 as cv
import numpy as np


def filterRedColor(image):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([180, 255, 255])
    mask1 = cv.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 | mask2
    red_filtered = cv.bitwise_and(image, image, mask=mask)
    return red_filtered


def getTargetValues(game_window, target_img):
    target = cv.imread(target_img)
    target_locked = cv.matchTemplate(game_window, target, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(target_locked)
    top_left = max_loc
    bot_right = (top_left[0] + target.shape[1], top_left[1] + target.shape[0])
    return {
        'max_val': max_val,
        'top_left': top_left,
        'bot_right': bot_right,
    }


def getItemValues(game_window, target_img):
    target = cv.imread(target_img)
    game_window_filtered = filterRedColor(game_window)
    target_filtered = filterRedColor(target)
    item_locked = cv.matchTemplate(game_window_filtered, target_filtered, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(item_locked)
    top_left = max_loc
    bot_right = (top_left[0] + target.shape[1], top_left[1] + target.shape[0])
    return {
        'max_val': max_val,
        'top_left': top_left,
        'bot_right': bot_right,
    }


def getTargetBorder_Center(game_window, top_left, bot_right, color):
    cv.rectangle(game_window, top_left, bot_right, color, thickness=2, lineType=cv.LINE_4)
    centers = (top_left[0] + bot_right[0]) // 2, (top_left[1] + bot_right[1]) // 2
    cv.drawMarker(game_window, centers, color=(135, 12, 236), markerType=cv.MARKER_CROSS)
    return centers

