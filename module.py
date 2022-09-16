import pyautogui as py
import time


def abrir_consultas():
    py.moveTo(252, 37)
    py.doubleClick()
    py.click(x=244, y=79)
    time.sleep(1)
    py.click(x=1177, y=650)
    while 1:
        consulta_pos = py.locateOnScreen('img/teladis.png')
        if consulta_pos:
            break