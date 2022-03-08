import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1

pyautogui.press("winleft")
pyautogui.write("chrome")
pyautogui.press("enter")



link = "https://www.youtube.com/watch?v=kgx4WGK0oNU&ab_channel=%E9%98%BF%E9%B2%8DAbao"

pyperclip.copy(link)
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")

time.sleep(4)


pyautogui.press("winleft")
pyautogui.write("Visual Studio Code")
pyautogui.press("enter")
time.sleep(5)
pyautogui.hotkey("ctrl","n")
time.sleep(2)
pyautogui.hotkey("ctrl","k")
pyautogui.hotkey("m")
pyautogui.write("Python")
pyautogui.press("tab")
pyautogui.press("enter")
