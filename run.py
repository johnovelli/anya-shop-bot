import keyboard
import ctypes

from config.intro_message import intro_message
from config.handle_bot import bot_process, start_bot, stop_bot, terminate_and_exit

# Set the console window title to "Anya Shop Bot 0.1"
ctypes.windll.kernel32.SetConsoleTitleW("Anya Shop Bot 0.1")

# Display the introductory message in the console
print(intro_message)

# Main loop to check for specific key presses to control the bot
while True:
    # Start the bot when F1 is pressed and no bot process is running
    if keyboard.is_pressed('F1') and bot_process is None:
        start_bot()
    # Stop the bot when F2 is pressed
    elif keyboard.is_pressed('F2'):
        stop_bot()
    # Terminate the bot and exit the program when F4 is pressed
    elif keyboard.is_pressed('F4'):
        terminate_and_exit()