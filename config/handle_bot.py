import subprocess
import sys
import time
import pygetwindow as gw


bot_process = None

def start_bot():
    global bot_process
    if bot_process is None:
        bot_process = subprocess.Popen(['python', 'main.py'])
        print("Bot started.")
        game_window = gw.getWindowsWithTitle("Diablo II: Resurrected")[0]
        bot_window = gw.getWindowsWithTitle("Anya shop bot 0.1")[0]
        if game_window:
            bot_window.maximize()
            time.sleep(0.5)
            game_window.activate()



def stop_bot():
    global bot_process
    if bot_process is not None:
        bot_process.terminate()
        bot_process = None
        print("Bot stopped.")


def terminate_and_exit():
    global bot_process
    if bot_process is not None:
        bot_process.terminate()
    sys.exit()
