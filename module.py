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
            print('Tela de Di Aberta')
            break


def fechar_inova():
    py.click(x=1556, y=251)
    print('Consultas bloqueadas')
    py.click(x=42, y=35)
    py.click(x=40, y=111)
    time.sleep(1)
    py.click(x=961, y=591)


#ALTERE A SENHA CASO USUÁRIO DIFERENTE.
def login_inova():
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


def data_consultas():
    py.click(x=392, y=405)
    py.write(dia_inicial)
    py.press('-')
    py.write(mes_inicial)
    py.press('tab')
    py.write(dia_final)
    py.press('-')
    py.write(mes_final)

def verifica_inova():
    py.click(x=658, y=1063)
    inova_open = py.locateOnScreen('img/inova_open.png')
    teladi_ativa = py.locateOnScreen('img/teladis.png')
    if inova_open:
        print('Inova já está Aberto!')
        if teladi_ativa:
            print('Tela de Di já aberta!')
        else:
            abrir_consultas()
    else:
        print('Abrindo Inova')
        login_inova()
        time.sleep(4)
        abrir_consultas()

def copiar_di():
    py.click(x=601, y=388)
    py.keyDown('ctrl')
    py.press('a')
    py.keyUp('ctrl')
    py.keyDown('ctrl')
    py.press('c')
    py.keyUp('ctrl')
    py.click(x=709, y=1058)
    py.press('enter')
    py.keyDown('ctrl')
    py.press('v')
    py.press('s')
    py.keyUp('ctrl')
    

