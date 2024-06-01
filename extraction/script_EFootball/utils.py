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

current_folder = os.path.dirname(os.path.abspath(__file__))

cursor_path = os.path.join(current_folder, '..', 'Templates', 'CURSOR.png')
depth_bis_path = os.path.join(current_folder, '..', 'Templates', 'depth_right.png')
end_game_path = os.path.join(current_folder, '..', 'Templates', 'end_pes_true.png')

cursor_template = cv2.imread(cursor_path, 0) 
depth_bis_template = cv2.imread(depth_bis_path, 0) 
end_game_template = cv2.imread(end_game_path, 0)

# =======================================================================================================
# ================= Principal method extracting repeatedly the color and depth data =====================
# =======================================================================================================

def extract_and_store_frames(video_folder, first_call, frame_count= 60):
    pydirectinput.click(x=886,y=440) # Clicks on the game screen 
    pydirectinput.press('f11') # Captures the frame
    time.sleep(10)

    if first_call:
       # Removes the message appearing only for the first capture #
       x,y = 1036, 645 
       time.sleep(2)
       first_call = False
       pydirectinput.click(x,y) 
  
    
    for _ in range(frame_count):

        # Saves the color image #
        x,y = 3277, 245
        time.sleep(9)
        pyautogui.click(x,y) # Clicks on the backleft button
        time.sleep(3) 
        save_create_folder(video_folder, 'color') 
        time.sleep(1)

        # Saves the color buffer #
        x,y = 2223, 179 
        pyautogui.click(x,y) # Clicks on the memory button
        time.sleep(0.5)
        save_create_folder(video_folder, 'color buffer')
        time.sleep(9)
        x,y = 3508, 445  # to click out of the window 
        pyautogui.click(x,y)
        time.sleep(0.5) 

        # Depth Extraction Part #
        x,y = 3000, 169 
        pyautogui.click(x,y)
        time.sleep(0.5)
        # Analysis the screen iteravely to find the button to access depth information # 
        security = 10
        depth_right_position = find_template_on_screen(depth_bis_template, False, threshold= 0.9)
        time.sleep(0.5)
        while not depth_right_position and security != 0:
            x = x + 8
            pyautogui.click(x,y)
            time.sleep(0.5)
            depth_right_position = find_template_on_screen(depth_bis_template, False, threshold=0.9)
            time.sleep(0.5)
            security  = security - 1
        if security == 0:
            break
        pyautogui.click(depth_right_position[0], depth_right_position[1])
        time.sleep(0.5)
        move_and_click_on_template(cursor_template) 
        time.sleep(0.5)

        # Saves the 8 bit normalized depth map #
        save_create_folder(video_folder, 'depth')
        time.sleep(1.5)
        pyautogui.click(x=2957,y=536) 
        time.sleep(1)

        # Saves the 16 bit unnormalized depth buffer #
        x,y = 2223, 179 
        pyautogui.click(x,y) # Clicks on the memory button
        time.sleep(0.5)
        save_create_folder(video_folder, 'depth buffer')
        time.sleep(10)

        # Go to the next frame and repeat
        x,y = 2421, 60
        pyautogui.click(x,y)
        time.sleep(10)


# =======================================================================================================
# ================= Methods to analyse screen and interact with the NVIDIA NSight tool ==================
# =======================================================================================================
'''
The following code has been adapted from the original codebase of the python_imagesearch library to fit the needs of the project.
The original codebase can be found at: https://github.com/drov0/python-imagesearch/blob/master/README.md

MIT License

Copyright (c) 2017 drov0
'''
def imagesearch_in_memory(template, precision=0.8):
    is_retina = False
    with mss.mss() as sct:
        im = sct.grab(sct.monitors[0])
        if is_retina:
            im.thumbnail((round(im.size[0] * 0.5), round(im.size[1] * 0.5)))
        img_rgb = np.array(im)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template.shape[::-1]
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # Déréférencement des images utilisées
        del img_rgb, img_gray

        if max_val < precision:
            return [-1, -1]
        return max_loc
    

def find_template_on_screen(template, screen_game, threshold=0.8):
    # Find a predefined element on the screen in the form of a given image with a certainty equal to the threshold. #
    if not screen_game:
        pyautogui.click(x=2700, y=380)
    else:
        pydirectinput.click(x=886,y=440)

    pos = imagesearch_in_memory(template, threshold)
    if pos[0] != -1:
        print(f"Position of the image is: {pos}")
        #pyautogui.click(pos[0], pos[1])
        return (pos[0], pos[1])
    else:
       print("Not found")
       return None

def move_and_click_on_template(cursor_template):
    # Move the cursor and click on the target template to extract the depth #
    cursor_position = find_template_on_screen(cursor_template, False)
    if not cursor_position:
        print("Curseur non trouvé sur l'écran.")
        return
    
    x,y = cursor_position[0]+3, cursor_position[1]

    # Move it towards the end of the rail
    pyautogui.moveTo(x,y)
    time.sleep(1)
    pyautogui.dragTo(3394, 896, button = 'left')
    time.sleep(1)
    pyautogui.click(3371, 816)
    time.sleep(1)



# ==============================================================================
# ================= Methods handling and creating folders ======================
# ==============================================================================

def save_create_folder(video_folder, subfolder):
    """
    This function handles the creation and saving of folders.  
    It generates also a unique filename and constructs the full file path. 
    """
    x,y = 2167, 151
    pyautogui.click(x,y) # to click on the save button
    filename = generate_unique_filename(video_folder, subfolder)
    file_path = os.path.join(video_folder, subfolder, filename)
    pyperclip.copy(file_path)
    time.sleep(1)
    pyautogui.hotkey('ctrl','v')
    time.sleep(1)
    pyautogui.press('enter')

def generate_unique_filename(video_folder, other):
    # Generate unique filename logic here, e.g., incremental names.
    subfolder = os.path.join(video_folder, other)
    existing_files = os.listdir(subfolder)
    counter = len(existing_files) + 1
    return f'{counter}'


def setup_folders(master, game_number, video_number):
    path = r'C:\Users\telim\OneDrive\Desktop'
    master_folder = os.path.join(path, master)
    game_folder = os.path.join(master_folder, f'game_{game_number}')
    video_folder = os.path.join(game_folder, f'video_{video_number}')
    subfolders = ['color', 'color buffer', 'depth', 'depth buffer']

    # Create master folder if it doesn't exist
    if not os.path.exists(master_folder):
        os.mkdir(master_folder)

    # Create game folder if it doesn't exist
    if not os.path.exists(game_folder):
        os.mkdir(game_folder)
        
    # Create video folder if it doesn't exist
    if not os.path.exists(video_folder):
        os.mkdir(video_folder)

    # Create subfolders
    for subfolder in subfolders:
        path = os.path.join(video_folder, subfolder)
        if not os.path.exists(path):
            os.mkdir(path)
    
    return video_folder


# ==============================================================================
# ================= Methods interacting with the NBA2K22 game ==================
# ==============================================================================

def start_game():
    pydirectinput.click(x=886,y=440)
    time.sleep(1)
    pydirectinput.press('enter')
    time.sleep(2)
    pydirectinput.press('enter')
    time.sleep(1)
    pydirectinput.press('w')  # switch once to pick a random team
    time.sleep(2)
    pydirectinput.press('enter')
    time.sleep(1)
    pydirectinput.press('w')  # switch once to pick a random team
    time.sleep(1)
    pydirectinput.press('enter')
    time.sleep(5)
    pydirectinput.press('a')
    time.sleep(1)
    pydirectinput.press('enter', presses = 2, interval = 1)
    time.sleep(1)
    pydirectinput.press('down', presses=6)
    time.sleep(4)
    pydirectinput.press('enter')
    time.sleep(1)
    pydirectinput.press('down')
    time.sleep(1)
    pydirectinput.press('enter')
    time.sleep(1)
    pydirectinput.press('down', presses=5)
    time.sleep(1)
    pydirectinput.press('enter')
    time.sleep(1)
    pydirectinput.press('d')
    time.sleep(3)
    pydirectinput.press('down', presses=2)
    time.sleep(1)
    pydirectinput.press('enter', presses = 2, interval = 1)
    time.sleep(1)
    pydirectinput.press('down', presses=14)
    time.sleep(1) 
    pydirectinput.press('up', presses=8)
    time.sleep(1)
    pydirectinput.press('enter')
    time.sleep(1)
    pydirectinput.press('d', presses=3, interval=1)
    time.sleep(1)
    pydirectinput.press('w')  # to go to stadium
    time.sleep(1)
    pydirectinput.press('down')
    time.sleep(1)
    pydirectinput.press('enter')
    time.sleep(1)
    pydirectinput.press('up')
    time.sleep(1)
    pydirectinput.press('enter')
    time.sleep(1)
    pydirectinput.press('enter')
    time.sleep(1)
    nbr = random.randint(0,1)
    if nbr == 1:
        pydirectinput.press('down')
        time.sleep(1)
    pydirectinput.press('enter')
    time.sleep(1)
    pydirectinput.press('down')
    time.sleep(1)
    pydirectinput.press('enter')
    time.sleep(1)
    pydirectinput.press('up')
    time.sleep(1)
    pydirectinput.press('enter')
    time.sleep(1)
    pydirectinput.press('enter')
    time.sleep(1)
    nbr1 = random.randint(0,1)
    if nbr1 == 1:
        pydirectinput.press('down')
        time.sleep(1)
    pydirectinput.press('enter')
    time.sleep(1)
    if nbr1 == 1:
        pydirectinput.press('down')
        time.sleep(1)
        pydirectinput.press('enter')
        time.sleep(1)
        pydirectinput.press('up', presses = 2, interval = 1)
        time.sleep(1)
        pydirectinput.press('enter')
        time.sleep(1)
        pydirectinput.press('enter')
        time.sleep(1)
        nbr_2 = random.randint(0,2)
        if nbr_2 != 0:
            pydirectinput.press('down', presses = nbr_2, interval = 1)
            time.sleep(1)
        pydirectinput.press('enter')
        time.sleep(1)
    if nbr1 == 0:
        pydirectinput.press('down')
        time.sleep(1)
        pydirectinput.press('enter')
        time.sleep(1)
        pydirectinput.press('up')
        time.sleep(1)
        pydirectinput.press('enter')
        time.sleep(1)
        pydirectinput.press('enter')
        time.sleep(1)
        nbr = random.randint(0,1)
        if nbr == 1:
            pydirectinput.press('down')
            time.sleep(1)
        pydirectinput.press('enter')
        time.sleep(1)
    pydirectinput.press('d')
    time.sleep(3)
    pydirectinput.press('enter')
    time.sleep(4)
    pydirectinput.press('enter')
    time.sleep(6)
    pydirectinput.press('enter')
    time.sleep(6)
    pydirectinput.press('enter', presses = 2) # skip cinematics
    time.sleep(6)
    pydirectinput.press('x', presses=3, interval=0.5) # first pass as we have the ball
    time.sleep(2)



def handle_game_end_sequence():
    end_game_template = cv2.imread(end_game, 0)
    time.sleep(3)
    pydirectinput.click(x=886,y=440)
    while not find_template_on_screen(end_game_template, True, threshold=0.9):
        pydirectinput.press('x')
        time.sleep(1)
    time.sleep(2)
    pydirectinput.press('down', presses = 2, interval=0.5)  # go down three times
    time.sleep(1)
    pydirectinput.press('x')  # confirm once
    time.sleep(5)
 




# ==============================================================================
# ============= Methods to test individually the functions =====================
# ==============================================================================
def test_function(func_name):
    if func_name == "choose_random_teams":
        start_game()
    elif func_name == "extract_and_store_frames":
        video_folder = setup_folders("1_PES", 1, 1)
        extract_and_store_frames(video_folder, False)
    elif func_name == "save_create_folder":
        video_folder = setup_folders("1_PES", 1, 1)
        save_create_folder(video_folder, 'color')
    elif func_name == "generate_unique_filename":
        video_folder = setup_folders("1_PES", 1, 1)
        print(generate_unique_filename(video_folder, 'color'))
    elif func_name == "handle_game_end_sequence":
        handle_game_end_sequence()
    elif func_name == "setup_folders":
        print(setup_folders("1_PES", 1, 1))
    elif func_name == "find_template_on_screen":
        print(find_template_on_screen(depth_bis_path))
    elif func_name == "move_and_click_on_template":
        move_and_click_on_template(cursor_path)
    else:
        print(f"Function {func_name} not found!")
        
def run_test_functions():
    while True:
        print("\nAvailable functions:")
        print("1. choose_random_teams")
        print("2. extract_and_store_frames")
        print("3. save_create_folder")
        print("4. generate_unique_filename")
        print("5. handle_game_end_sequence")
        print("6. setup_folders")
        print("7. find_template_on_screen")
        print("8. move_and_click_on_template")
        print("0. Exit")
        
        choice = input("Enter the function number you want to test (or 0 to exit): ")
        
        if choice == "1":
            test_function("choose_random_teams")
            break
        elif choice == "2":
            test_function("extract_and_store_frames")
        elif choice == "3":
            test_function("save_create_folder")
        elif choice == "4":
            test_function("generate_unique_filename")
        elif choice == "5":
            test_function("handle_game_end_sequence")
        elif choice == "6":
            test_function("setup_folders")
        elif choice == "7":
            test_function("find_template_on_screen")
        elif choice == "8":
            test_function("move_and_click_on_template")
        elif choice == "0":
            break
        else:
          print("Invalid choice!")
