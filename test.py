from statistics import linear_regression
import pyautogui as py
from PIL import Image
import time
import module
import gc
from datetime import datetime


di_perdidas = open('teste.txt', 'r')
conteudo = di_perdidas.readlines()

py.click(x=715, y=1060)
py.click(x=380, y=325)

py.keyDown('ctrl') 
py.keyDown('shift')
py.press(['right', 'right', 'right'])
py.keyUp('ctrl')
py.keyUp('shift')