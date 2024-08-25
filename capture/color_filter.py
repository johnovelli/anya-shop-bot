import cv2 as cv
import numpy as np


def filterRedColor(image):
    # Convert the image to HSV color space
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    # Define the range for detecting red color
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([180, 255, 255])

    # Create masks for the red color ranges
    mask1 = cv.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 | mask2

    # Apply the mask to filter out the red color from the image
    red_filtered = cv.bitwise_and(image, image, mask=mask)

    return red_filtered

# def filterYellowColor(image):
#     # Convert the image to HSV color space
#     hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

#     # Define the range for detecting yellow color
#     lower_yellow1 = np.array([15, 100, 100])
#     upper_yellow1 = np.array([25, 255, 255])
#     lower_yellow2 = np.array([25, 70, 70])
#     upper_yellow2 = np.array([35, 255, 255])

#     # Create masks for the yellow color ranges
#     mask1 = cv.inRange(hsv, lower_yellow1, upper_yellow1)
#     mask2 = cv.inRange(hsv, lower_yellow2, upper_yellow2)
#     mask = mask1 | mask2

#     # Apply the mask to filter out the yellow color from the image
#     yellow_filtered = cv.bitwise_and(image, image, mask=mask)

#     return yellow_filtered