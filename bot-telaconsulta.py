from select import select
import pyautogui as py
import time
import module
from PIL import Image
import selectLetras
currentMouseX, currentMouseY = py.position()

#ABRINDO A CONSULTA DE DI'S
module.verifica_inova()

#CONFIGURANDO DATA
module.data_consultas()

#Selecionar ultima opção tela consultas
#selectLetras.selecionar_letraD()

py.click(x=414, y=342)


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
        



