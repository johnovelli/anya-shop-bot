import keyboard
import ctypes

from config.intro_message import intro_message
from config.handle_bot import bot_process, start_bot, stop_bot, terminate_and_exit


ctypes.windll.kernel32.SetConsoleTitleW("Anya Shop Bot 0.1")


print(intro_message)


while True:
    if keyboard.is_pressed('F1') and bot_process is None:
        start_bot()
    elif keyboard.is_pressed('F2'):
        stop_bot()
    elif keyboard.is_pressed('F4'):
        terminate_and_exit()
