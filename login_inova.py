import pyautogui as py
import time

py.click(x=658, y=1063)
while 1:
    login_pos = py.locateOnScreen('img/login.png')
    if login_pos:
        py.press('tab')
        py.write('pp348247')
        py.press('enter')
        print('Conta Acessada')
        time.sleep(3)
        py.click(x=1406, y=267)
        break

    
