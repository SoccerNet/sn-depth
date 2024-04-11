import pyautogui
import pydirectinput

print("======================================")
print("Position Checker")
print("======================================")
print("Instructions:")
print("1. Move the mouse to the desired position.")
print("2. Press Enter.")
input("Press Enter when ready...")

position = pyautogui.position()

print("\n======================================")
print(f"The position of the cursor is: {position}")
print("======================================")