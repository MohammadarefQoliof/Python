import pyautogui
import keyboard
import time

while True:
    if keyboard.is_pressed('q'):
        break
    else:
        x, y = pyautogui.position()
        print(f"Mouse position: x={x}, y={y}", end='\r')
        time.sleep(0.1)

time.sleep(1)
pyautogui.hotkey("win", "d")
time.sleep(1)
pyautogui.moveTo(148, 900, duration=2)
time.sleep(0.5)
pyautogui.doubleClick()
time.sleep(1)
pyautogui.moveTo(430, 242, duration=2)
time.sleep(0.5)
pyautogui.doubleClick()