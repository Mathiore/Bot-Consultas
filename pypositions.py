import pyautogui as py
from PIL import Image
import time
import module

screenWidth, screenHeight = py.size()
currentMouseX, currentMouseY = py.position()

print(py.position())

py.click(x=1144, y=255)
bloco_notas = py.locateOnScreen('img/bloco_notas.png', confidence=0.9)
py.click(bloco_notas)
ref_position = py.locateOnScreen('img/position_bloco.png', confidence=0.9)
time.sleep(1)
print(ref_position)
time.sleep(1)


py.click(x=ref_position.left, y=ref_position.top+25)

