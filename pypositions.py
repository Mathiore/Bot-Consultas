import pyautogui as py
from PIL import Image
import time
import module

screenWidth, screenHeight = py.size()
currentMouseX, currentMouseY = py.position()

print(py.position())

py.click(x=683, y=537)

linha = 2

while 1:
    icon_pos = py.locateOnScreen('img/concluidosingle.png')
    bloqueio = py.locateOnScreen('img/bloqueiosingle.png')
    bloco_notas = py.locateOnScreen('img/bloco_notas.png', confidence= 0.9)
    ref_position = py.locateOnScreen('img/position_bloco.png', confidence= 0.9)
    if icon_pos:
        py.click(x=1046, y=596)
        print('Concluido!')
        break
    elif bloqueio:
        print('Falhou!')
        print('Apagando DIs Concluídas.')
        i = 0
        py.click(bloco_notas)
        py.click(x=ref_position.left, y=ref_position.top+25)
        while i < linha:
            py.keyDown('ctrl') 
            py.keyDown('shift')
            py.press(['right', 'right', 'right'])
            py.keyUp('ctrl')
            py.keyUp('shift')
            py.press('backspace')
            i = i + 1
            py.click(x=1394, y=285)