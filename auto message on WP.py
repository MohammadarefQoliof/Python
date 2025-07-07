import pyautogui
import time

# time.sleep(3)
# x, y = pyautogui.position()
# print(f"Mouse position: x={x}, y={y}")
# time.sleep(0.1)

message = input("Enter message: ")
attempt = int(input("Enter number: "))
person = input("Enter the contact name: ")

time.sleep(0.5)

pyautogui.moveTo(1071, 1054, duration=2)
time.sleep(0.5)

pyautogui.click()
time.sleep(0.5)

pyautogui.moveTo(342, 149, duration=2)
time.sleep(0.5)

pyautogui.click()
time.sleep(0.5)

pyautogui.write(person, interval=0.15)
time.sleep(0.5)

pyautogui.moveTo(296, 232, duration=2)
time.sleep(2)

pyautogui.click()
time.sleep(0.5)

pyautogui.moveTo(709, 986, duration=2)
time.sleep(0.5)

pyautogui.click()
time.sleep(0.5)

while attempt > 0:
    pyautogui.write(message, interval=0.05)
    time.sleep(0.5)
    pyautogui.press("enter")
    attempt = attempt - 1
    time.sleep(0.5)