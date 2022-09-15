import pyautogui as py
import time
from PIL import Image

currentMouseX, currentMouseY = py.position()

print(py.position())


#COMANDOS DE TECLADO ALTERAÇÃO DE JANELA
#py.keyDown('alt')
#py.press('tab')
#py.keyUp('alt')

#COMANDOS DE MOUSE
#ABRINDO A CONSULTA DE DI'S
py.moveTo(252, 37)
py.doubleClick()
py.click(x=244, y=79)
time.sleep(1)
py.click(x=1177, y=650)
time.sleep(17)

#CONFIGURANDO DATA
py.click(x=392, y=405)
py.write('21')
py.press('-')
py.write('08')
py.press('tab')
py.write('25')
py.press('-')
py.write('08')

py.click(x=382, y=477)

n = 4
i = 0

while i < n:
    py.press('space')

    py.press('down', presses=2)

    i = i+1

py.click(x=414, y=342)

icon_pos = py.locateOnScreen('alertaconcluido.png')

wait_icon = 1
while 1:
    if icon_pos:
        py.click(x=1054, y=597)
        print('Consulta Finalizada')
        py.click(x=1326, y=278)
        wait_icon = 0

py.click(x=582, y=769)



