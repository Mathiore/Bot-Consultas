import pyautogui as py



#SELECIONAR TODOS DA LETRA A
def selecionar_letraA():
    py.click(x=402, y=475)

    #PULA ASCENSUS/ASGARD/ATM
    j = 0
    x = 14
    while j < x:
        py.press('space')

        py.press('down', presses=2)

        j = j+1

#SELECIONAR TODOS DA LETRA B
def selecionar_letraB():
    py.click(x=398, y=715)
    i=0
    n = 1
    while i <= n:
        py.press('down')
        i = i+1

    j = 0
    x = 18
    while j < x:
        py.press('space')

        py.press('down', presses=2)

        j = j+1


#SELECIONAR TODOS DA LETRA C
def selecionar_letraC():
    py.click(x=398, y=715)

    i=0
    n = 19
    while i <= n:
        py.press('down')
        i = i+1

    j = 0
    x = 19
    while j < x:
        py.press('space')

        py.press('down', presses=2)

        j = j+1


#SELECIONAR TODOS DA LETRA D
def selecionar_letraD():
    py.click(x=398, y=715)
    i=0
    n = 38
    while i <= n:
        py.press('down')
        i = i+1

    j = 0
    x = 7
    while j < x:
        py.press('space')

        py.press('down', presses=2)

        j = j+1


