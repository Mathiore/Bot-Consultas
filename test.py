from statistics import linear_regression
import pyautogui as py
from PIL import Image
import time
import module
import gc
from datetime import datetime


di_perdidas = open('dis_perdidas.txt', 'r')
conteudo = di_perdidas.readlines()

line = 0

print(conteudo[line])


py.click(x=709, y=1058)
py.press('enter')
py.write(conteudo[line])