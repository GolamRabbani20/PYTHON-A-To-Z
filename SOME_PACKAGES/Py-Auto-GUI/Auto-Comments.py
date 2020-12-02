import pyautogui
import time

comments = ["Hi","Just commenting for fun","I am commenting by python programming","ki korish?",
            "I am just checking my python skill","python is awesome","I love programme",'kobe asbi??']

time.sleep(5)
for i in range(10):
    pyautogui.typewrite(comments[i%len(comments)])
    pyautogui.typewrite("\n")
    time.sleep(2)