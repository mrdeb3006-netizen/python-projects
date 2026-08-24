import pyautogui
import time
import random

time.sleep(5)

for i in range(10):
    watch_time= random.randint(15,25)
    time.sleep(watch_time)
    pyautogui.press("down")
    