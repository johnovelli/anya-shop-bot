import cv2 as cv

from capture.capture_window import capture_game_window
from main_process.anya_process import processAnya
from main_process.shop_process import shopProcess

is_trade_open = False

while True:

    try:
        game_window = capture_game_window("Diablo II: Resurrected")

        if not is_trade_open:
            is_trade_open = processAnya(game_window)
        if is_trade_open:
            is_trade_open = shopProcess(game_window)
        # height, width = game_window.shape[:2]
        # resized_game_window = cv.resize(game_window, (width // 2, height // 2))
        # ImageGrab.grab(cv.imshow('Computer Vision', resized_game_window))

    except Exception as e:
        print(f"An error occurred: {e}")

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
