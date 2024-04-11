
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

from utils import cursor_path, depth_path, depth_bis_path, end_game_path, cursor_template, depth_bis_template, depth_path_template
from utils import *


def main():
    TOTAL_GAMES = 1000
    VIDEOS_PER_GAME = 10
    GAME_DURATION = 4 * 60 

    master = "1_NBA"
    # Go through the NBA2K menu
    pydirectinput.click(x=917, y = 605)
    time.sleep(1)
    pydirectinput.press('3')
    time.sleep(1)
    pydirectinput.press('right', presses=2) 
    time.sleep(1)
    pydirectinput.press('2')
    first_call = True

    path = r'C:\Users\telim\OneDrive\Desktop'
    master_folder = os.path.join(path, master)
    existing_files = os.listdir(master_folder)
    counter = len(existing_files) + 1


    for game_number in range(counter, TOTAL_GAMES + 1):
        choose_random_teams()
        time.sleep(10) 
        pass_cinematics()
        for video_number in range(1, VIDEOS_PER_GAME + 1):
            video_folder = setup_folders(master, game_number, video_number)
            time.sleep(3)
            for _ in range(20):
                extract_and_store_frames(video_folder, first_call)
                time.sleep(3)
                pyautogui.click(x=2507, y=58) # Resume the game
                time.sleep(2.5) 
            pyautogui.click(x=2507, y=58) 
            time.sleep(0.5)
            first_call = False
        handle_game_end_sequence()
        time.sleep(10) # Delay before starting the next game. 


if __name__ == "__main__":
    # run_test_functions()
    main()
    

