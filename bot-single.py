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
    retifica_btn = py.locateOnScreen('img/botao_retificacao.png')
    if retifica_btn:
        py.click(x=1123, y=491)
        break


py.click(x=1132, y=525)

py.click(button='right')

py.click(x=1146, y=530)

py.click(x=1177, y=650)

time.sleep(2)

py.click(x=535, y=324)

while 1:
    icon_pos = py.locateOnScreen('img/alertaconcluido.png')
    if icon_pos:
        py.click(x=1046, y=596)
        py.click(x=1403, y=289)
        break

