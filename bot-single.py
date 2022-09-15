import pyautogui as py
from PIL import Image
import time
screenWidth, screenHeight = py.size()
currentMouseX, currentMouseY = py.position()

print(py.position())

py.keyDown('alt')
py.press('tab')
py.keyUp('alt')

