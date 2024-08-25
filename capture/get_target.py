import cv2 as cv
import numpy as np


def getTargetValues(game_window, target_img):
    # Load the target image and perform template matching on the game window
    target = cv.imread(target_img)
    target_locked = cv.matchTemplate(game_window, target, cv.TM_CCOEFF_NORMED)

    # Get the minimum and maximum match values and their locations
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(target_locked)

    # Calculate the coordinates of the top-left and bottom-right corners
    top_left = max_loc
    bot_right = (top_left[0] + target.shape[1], top_left[1] + target.shape[0])

    # Return a dictionary with match values and coordinates
    return {
        'max_val': max_val,
        'top_left': top_left,
        'bot_right': bot_right,
    }


def getItemValues(game_window, target_img, threshold, color_filter):
    # Load the target image and apply the color filter to the game window and the target
    target = cv.imread(target_img)
    game_window_filtered = color_filter(game_window)
    target_filtered = color_filter(target)

    # Perform template matching with the filtered images
    item_locked = cv.matchTemplate(game_window_filtered, target_filtered, cv.TM_CCOEFF_NORMED)

    armor_values_list = []

    # Identify locations where the match is above or equal to the threshold
    locations = np.where(item_locked >= threshold)

    # For each location found, calculate the coordinates and check for duplicates
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

    # Return the list of item match values
    return armor_values_list


def getTarget_Center(game_window, top_left, bot_right, color):
    # Draw a rectangle around the target and calculate its center
    cv.rectangle(game_window, top_left, bot_right, color, thickness=2, lineType=cv.LINE_4)
    centers = (top_left[0] + bot_right[0]) // 2, (top_left[1] + bot_right[1]) // 2

    # Return the coordinates of the target's center
    return centers