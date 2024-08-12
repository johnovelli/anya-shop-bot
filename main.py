import cv2 as cv
from PIL import ImageGrab
from capture_window import capture_game_window


while True:
    try:
        game_window = capture_game_window("Diablo II: Resurrected")

        height, width = game_window.shape[:2]
        resized_game_window = cv.resize(game_window, (width // 2, height // 2))
        ImageGrab.grab(cv.imshow('Computer Vision', resized_game_window))

    except Exception as e:
        print(f"An error occurred: {e}")

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
