from statistics import linear_regression
import pyautogui as py
from PIL import Image
import time
import module
import gc
from datetime import datetime

py.click(x=1144, y=288)
while 1:
    bloco_notas = py.locateOnScreen('img/bloco_notas.png')
    if bloco_notas:
        py.click(bloco_notas)
        break
