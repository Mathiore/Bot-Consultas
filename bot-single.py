import pyautogui as py
from PIL import Image
import time
screenWidth, screenHeight = py.size()
currentMouseX, currentMouseY = py.position()

print(py.position())

py.keyDown('alt')
py.press('tab')
py.keyUp('alt')



while 1:
    icon_pos = py.locateOnScreen('alertaconcluido.png')
    if icon_pos:
        py.click(x=1054, y=597)
        print('Consulta Finalizada')
        break
        
py.click(x=1326, y=278)