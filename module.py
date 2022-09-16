import pyautogui as py
import time


dia_inicial = '16'
dia_final = '20'

mes_inicial = '08'
mes_final = '08'

#necessário implementar no futuro caso for preciso.
ano_inicial = '2022'
ano_final = '2022'

def abrir_consultas():
    py.click(x=252, y=37)
    py.click(x=244, y=79)
    time.sleep(1)
    py.click(x=1177, y=650)
    while 1:
        consulta_pos = py.locateOnScreen('img/teladis.png')
        if consulta_pos:
            break


def fechar_inova():
    py.click(x=1556, y=251)
    print('Consultas bloqueadas')
    py.click(x=42, y=35)
    py.click(x=40, y=111)
    py.doubleClick(x=961, y=591)


def login_inova():
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


def datas_single():
    py.press('tab')
    py.press('space')
    py.click(x=405, y=401)
    py.write(dia_inicial)
    py.press('-')
    py.write(mes_inicial)
    py.press('tab')
    py.press('space')
    py.click(x=535, y=401)
    py.write(dia_final)
    py.press('-')
    py.write(mes_final)
    py.click(x=386, y=340)

def verifica_inova():
    inova_open = py.locateOnScreen('img/inova_open.png')
    if inova_open:
        print('Inova já está Aberto!')
    else:
        print('Abrindo Inova')
        login_inova()

    time.sleep(1)
    teladi_ativa = py.locateOnScreen('img/teladis.png')
    if teladi_ativa:
        print('Tela de Di já aberta!')
    else:
        abrir_consultas()
    