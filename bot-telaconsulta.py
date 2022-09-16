import pyautogui as py
import time
import module
from PIL import Image

currentMouseX, currentMouseY = py.position()

print(py.position())


#COMANDOS DE TECLADO ALTERAÇÃO DE JANELA
#py.keyDown('alt')
#py.press('tab')
#py.keyUp('alt')

#COMANDOS DE MOUSE
#ABRINDO A CONSULTA DE DI'S
module.abrir_consultas()

#CONFIGURANDO DATA
py.click(x=392, y=405)
py.write('16')
py.press('-')
py.write('08')
py.press('tab')
py.write('20')
py.press('-')
py.write('08')

#Comando para a letra C
py.click(x=398, y=715)

i=0
n = 19
while i <= n:
    py.press('down')
    i = i+1

j = 0
x = 19
while j < x:
    py.press('space')

    py.press('down', presses=2)

    j = j+1

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
        break
        
py.click(x=1326, y=278)



