import pyautogui as py
import time

currentMouseX, currentMouseY = py.position()

di_perdidas = open('dis_perdidas.txt', 'r')
conteudo = di_perdidas.readlines()
linha = 0
print(py.position())