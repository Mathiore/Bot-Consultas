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

inova_open = py.locateOnScreen('img/inova_open.png')
if inova_open:
    print('Inova já está Aberto!')
else:
    print('Abrindo Inova')
    module.login_inova()

time.sleep(1)
teladi_ativa = py.locateOnScreen('img/teladis.png')
if teladi_ativa:
    print('Tela de Di já aberta!')
else:
    py.keyDown('alt')
    py.press('tab')
    py.keyUp('alt')
    module.abrir_consultas()

#Clica na aba de Di's
py.click(x=586, y=313)

module.datas_single()

while 1:
    retifica_btn = py.locateOnScreen('img/botao_retificacao.png')
    if retifica_btn:
        py.click(x=1123, y=491)
        break


position_x = 1132 
position_y = 525
i = 0
n = 5

while i < n:
    py.click(x=position_x, y=position_y)
    py.click(button='right')
    py.click(x=position_x+12, y=position_y+5)
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
                    time.sleep(0.5)
                    py.click(x=1125, y=728)
                    module.fechar_inova()
                    break
        elif icon_pos:
            py.click(x=1046, y=596)
            py.click(x=1403, y=289)
            break
    position_x = position_x+2
    position_y = position_y+20
    py.click(x=position_x, y=position_y)
    



