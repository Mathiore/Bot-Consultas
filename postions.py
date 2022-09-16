import pyautogui as py


print(py.position())

py.keyDown('alt')
py.press('tab')
py.keyUp('alt')

while 1:
    bloqueio = py.locateOnScreen('img/bloqueiosingle.png')
    if bloqueio:
        py.click(x=1403, y=289)
        break