
import pydirectinput
from python_imagesearch.imagesearch import imagesearch
import pyperclip
import pyautogui
import time
import random
import os
import cv2
import numpy as np
import mss
from utils import *


def main():
    TOTAL_GAMES = 1000
    VIDEOS_PER_GAME = 3
    GAME_DURATION = 10 * 60  # 24 minutes in seconds.

    master = "1_PES"
    # the first step is to go to trial match and then click enter
    pydirectinput.click(x=917, y = 605)
    first_call = True


    path = r'C:\Users\telim\OneDrive\Desktop'
    master_folder = os.path.join(path, master)
    existing_files = os.listdir(master_folder)
    counter = len(existing_files) + 1

    for game_number in range(counter, TOTAL_GAMES + 1):
        start_game()
        time.sleep(2) 
        for video_number in range(1, VIDEOS_PER_GAME + 1):
            video_folder = setup_folders(master, game_number, video_number)
            time.sleep(3)
            for _ in range (15):
                extract_and_store_frames(video_folder, first_call)
                time.sleep(3) 
                pyautogui.click(x=2507, y=58) # Resume game
                time.sleep(2.5) 
                pydirectinput.click(x=886,y=440) # Click on the game
                time.sleep(0.75)
                pydirectinput.press('x', presses = 3, interval = 0.5) # Pass the half time or cinematics
                pydirectinput.press('x', presses = 5, interval = 0.3) 
            pyautogui.click(x=2507, y=58) 
            time.sleep(0.5)
            first_call = False
        handle_game_end_sequence()
        time.sleep(10) # Delay before starting the next game. 


if __name__ == "__main__":
    #run_test_functions()
    main()
