from pynput.keyboard import Key, Controller
#pip install pynput
import time
keyboard = Controller()

#time.sleep(5)
while True:
    keyboard.press(Key.space)  # spacebar key press
    keyboard.release(Key.space)  # spacebar key release
    time.sleep(2)  # 2 সেকেন্ড বিরতি
