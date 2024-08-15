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


def filterYellowColor(image):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    mask = cv.inRange(hsv, lower_yellow, upper_yellow)
    yellow_filtered = cv.bitwise_and(image, image, mask=mask)
    return yellow_filtered


def filterGrayColor(image):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    lower_gray = np.array([0, 0, 180])
    upper_gray = np.array([180, 50, 255])
    lower_dark_gray = np.array([0, 0, 50])
    upper_dark_gray = np.array([180, 50, 100])
    mask_light_gray = cv.inRange(hsv, lower_gray, upper_gray)
    mask_dark_gray = cv.inRange(hsv, lower_dark_gray, upper_dark_gray)
    mask = cv.bitwise_or(mask_light_gray, mask_dark_gray)
    gray_filtered = cv.bitwise_and(image, image, mask=mask)
    return gray_filtered
