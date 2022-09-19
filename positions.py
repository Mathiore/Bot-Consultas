import pyautogui as py
import time

currentMouseX, currentMouseY = py.position()

di_perdidas = open('dis_perdidas.txt', 'r')
conteudo = di_perdidas.readlines()
linha = 0

py.click(x=1132, y=525)
py.click(button='right')
py.click(x=1144, y=530)
time.sleep(1)