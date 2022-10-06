import pyautogui as py
from PIL import Image
import time
import module

screenWidth, screenHeight = py.size()
currentMouseX, currentMouseY = py.position()

print(py.position())


with open('teste.txt', 'r+') as file:
    di = file.readlines()
    file.seek(0)
    for linhas in di:
        if linhas != di[linha]:
            file.write(linhas)
    file.truncate()        

#y.click(x=ref_position.left, y=ref_position.top+35)