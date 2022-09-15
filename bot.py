import pyautogui

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

print(pyautogui.position())

pyautogui.moveTo(3050, 527)
