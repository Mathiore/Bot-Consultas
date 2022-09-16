import pyautogui as py
from PIL import Image
import time
import module
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

position_x = 1132 
position_y = 525
consult_x = 1144
consult_y = 530
i = 0
n = 10

while i < n:
    print(py.position())
    py.click(x=position_x, y=position_y)
    print(py.position())
    py.click(button='right')
    py.click(x=consult_x, y=consult_y)
    print(py.position())
    time.sleep(1)
    py.click(x=1177, y=650)
    time.sleep(2)
    py.click(x=535, y=324)
    while 1:
        icon_pos = py.locateOnScreen('img/concluidosingle.png')
        retificado = py.locateOnScreen('img/retificado.png')
        bloqueio = py.locateOnScreen('img/bloqueiosingle.png')
        if bloqueio:
            py.click(x=1403, y=289)
            while 1:
                if bloqueio:
                    py.click(x=1196, y=705)
                    time.sleep(1)
                    py.click(x=1125, y=728)
                    module.fechar_inova()
                    break
        elif icon_pos:
            py.click(x=1046, y=596)
            py.click(x=1403, y=289)
            break
        elif retificado:
            print('Consultas já Finalizadas')
            break
    position_x = position_x+2
    position_y = position_y+20
    consult_x = consult_x+5
    consult_y = consult_y+30
    time.sleep(5)
