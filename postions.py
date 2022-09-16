import pyautogui as py


print(py.position())

py.keyDown('alt')
py.press('tab')
py.keyUp('alt')

while 1:
    icon_pos = py.locateOnScreen('img/alertaconcluido.png')
    if icon_pos:
        py.click(x=1046, y=596)
        py.click(x=1403, y=289)
        break