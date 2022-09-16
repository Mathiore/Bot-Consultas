import pyautogui as py
from PIL import Image
import time
import module
screenWidth, screenHeight = py.size()
currentMouseX, currentMouseY = py.position()

print(py.position())
#py.keyDown('alt')
#py.press('tab')
#py.keyUp('alt')


py.click(x=586, y=329)

while 1:
    consulta_pos = py.locateOnScreen('img/teladis.png')
    if consulta_pos:
        print('Tela de Di Aberta')
        break