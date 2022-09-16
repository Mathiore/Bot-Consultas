import pyautogui as py
from PIL import Image
import time
import module
screenWidth, screenHeight = py.size()
currentMouseX, currentMouseY = py.position()

print(py.position())

py.click(x=658, y=1063)

while 1:
    icon_pos = py.locateOnScreen('img/alertaconcluido.png')
    blockicon_pos = py.locateOnScreen('img/teladebloqueio.png')
    if blockicon_pos:
        py.click(x=1556, y=251)
        print('Consultas bloqueadas')
        py.click(x=42, y=35)
        py.click(x=40, y=111)
        py.click(x=961, y=591)
        break
    elif icon_pos:
        py.click(x=1054, y=597)
        print('Consulta Finalizada')
        time.sleep(1)
        py.click(x=1326, y=278)
        break