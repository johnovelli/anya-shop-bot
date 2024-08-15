import cv2 as cv
import numpy as np


def getTargetBorder_Center(game_window, top_left, bot_right, color):
    cv.rectangle(game_window, top_left, bot_right, color, thickness=2, lineType=cv.LINE_4)
    centers = (top_left[0] + bot_right[0]) // 2, (top_left[1] + bot_right[1]) // 2
    cv.drawMarker(game_window, centers, color=(135, 12, 236), markerType=cv.MARKER_CROSS)
    return centers


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


def getItemValues(game_window, target_img, color_filter):
    target = cv.imread(target_img)
    game_window_filtered = color_filter(game_window)
    target_filtered = filter(target)
    item_locked = cv.matchTemplate(game_window_filtered, target_filtered, cv.TM_CCOEFF_NORMED)
    armor_values_list = []
    locations = np.where(item_locked >= 0.8)
    for loc in zip(*locations[::-1]):
        top_left = loc
        bot_right = (top_left[0] + target.shape[1], top_left[1] + target.shape[0])
        max_val = item_locked[top_left[1], top_left[0]]
        if not any(existing['bot_right'][0] == bot_right[0] for existing in armor_values_list):
            armor_values_list.append({
                'max_val': max_val,
                'top_left': top_left,
                'bot_right': bot_right,
            })
    return armor_values_list


