import cv2 as cv

from capture.capture_window import capture_game_window
from main_process.anya_process import processAnya
from main_process.shop_process import shopProcess


# Initialize the trade status
is_trade_open = False

while True:
    try:
        # Capture the game window to analyze the current screen state
        game_window = capture_game_window("Diablo II: Resurrected")

        # Process Anya's shop and check if the trade screen is open
        if not is_trade_open:
            is_trade_open = processAnya(game_window)

        # If the trade screen is open, process the shop interactions
        if is_trade_open:
            is_trade_open = shopProcess(game_window)

    except Exception as e:
        # Handle any exceptions and print the error message
        print(f"An error occurred: {e}")

    # Check if the 'q' key is pressed to exit the loop and close windows
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break