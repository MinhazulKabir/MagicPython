import pyautogui
#pip install pyautogui
import time
import random
a_list=["How are you?", "Hello", "Hi",
        "asas", "valo"]

time.sleep(5)
while True:
    pyautogui.typewrite(f"{a_list[random.randint(0, 4)]}")
    pyautogui.press("enter")
