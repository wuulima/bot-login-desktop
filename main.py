from turtle import position
import pyautogui
import time

pyautogui.PAUSE = 2

pyautogui.press("win")
pyautogui.write("WhatsApp")
pyautogui.press("backspace")
pyautogui.press("enter")
pyautogui.click("x=979, y=250")
pyautogui.write("Minha Vida")

#time.sleep(5)
#print(pyautogui.position())