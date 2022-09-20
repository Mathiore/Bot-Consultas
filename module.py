from re import S
import pyautogui as py
import time
import gc
from datetime import datetime

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
def login_inova(usuario, senha):
    while 1:
        login_pos = py.locateOnScreen('img/login.png')
        if login_pos:
            py.press('backspace')
            py.write(usuario)
            py.press('tab')
            py.write(senha)
            py.press('enter')
            print('Conta Acessada')
            time.sleep(3)
            py.click(x=1406, y=267)
            break


def datas_single(dia_inicial, mes_inicial, dia_final, mes_final):
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


def data_consultas(dia_inicial, mes_inicial, dia_final, mes_final):
    py.click(x=392, y=405)
    py.write(dia_inicial)
    py.press('-')
    py.write(mes_inicial)
    py.press('tab')
    py.write(dia_final)
    py.press('-')
    py.write(mes_final)

def verificatela_di():
    teladi_ativa = py.locateOnScreen('img/teladis.png')
    if teladi_ativa:
        print('Tela de DI já aberta.')
    else:
        abrir_consultas()

def verifica_inova(usuario, senha):
    inova_icon = py.locateOnScreen('img/inova_icon.png')
    py.click(inova_icon)
    inova_open = py.locateOnScreen('img/inova_open.png')
    if inova_open:
        print('Inova já está Aberto!')
    else:
        print('Abrindo Inova')
        login_inova(usuario, senha)
        time.sleep(4)

def copiar_di():
    bloco_notas = py.locateOnScreen('img/bloco_notas.png')
    py.click(x=601, y=388)
    py.hotkey('ctrl','a')
    py.hotkey('ctrl','c')
    py.click(bloco_notas)
    py.press('enter')
    py.keyDown('ctrl')
    py.press('v')
    py.press('s')
    py.keyUp('ctrl')
    

def consulta_porLinhas(usuario, senha, dia_inicial, mes_inicial, dia_final, mes_final):
    linha = 0
    while 1:

        di_perdidas = open('dis_perdidas.txt', 'r')
        conteudo = di_perdidas.readlines()

        verifica_inova(usuario, senha)
        print('Continuando')
        verificatela_di()
        print('falha')

        #Clica na aba de Di's
        py.click(x=586, y=313)

        datas_single(dia_inicial, mes_inicial, dia_final, mes_final)

        while 1:
            retifica_btn = py.locateOnScreen('img/botao_retificacao.png')
            if retifica_btn:
                break
        py.click(x=1132, y=525)
        py.click(button='right')
        py.click(x=1144, y=530)
        time.sleep(1)
        py.click(x=1177, y=650)
        while 1:
            time.sleep(8)
            siscomex = py.locateOnScreen('img/aberto_consulta.png')
            if siscomex:
                break
            else:
                print('Ocorreu algum erro ao abrir o Siscomex.')
                py.click(x=1394, y=285)
                fechar_inova()
                gc.collect()
                consulta_porLinhas()
        total_linhas = len(conteudo)
        while linha <= total_linhas:
            py.click(x=597, y=390)
            py.hotkey('ctrl', 'a')
            py.press('backspace')
            py.write(conteudo[linha])
            time.sleep(1)
            py.click(x=535, y=324)
            print('Consultando: ', conteudo[linha])
            linha = linha + 1
            while 1:
                icon_pos = py.locateOnScreen('img/concluidosingle.png')
                bloqueio = py.locateOnScreen('img/bloqueiosingle.png')
                bloco_notas = py.locateOnScreen('img/bloco_notas.png', confidence= 0.9)
                ref_position = py.locateOnScreen('img/position_bloco.png', confidence= 0.9)
                if icon_pos:
                    py.click(x=1046, y=596)
                    print('Concluido!')
                    break
                elif bloqueio:
                    print('Falhou!')
                    print('Apagando DIs Concluídas.')
                    i = 0
                    py.click(bloco_notas)
                    py.click(x=ref_position.left, y=ref_position.top+25)
                    while i < linha:
                        py.keyDown('ctrl') 
                        py.keyDown('shift')
                        py.press(['right', 'right', 'right'])
                        py.keyUp('ctrl')
                        py.keyUp('shift')
                        py.press('backspace')
                        i = i + 1
                    py.click(x=1394, y=285)
                    fechar_inova()
                    time.sleep(1800)
                    now = datetime.now()
                    timestamp = datetime.timestamp(now)
                    print('Já se passaram 30 minutos!')
                    print('Realizando Limpeza de memória!')
                    print("Horário agora: ", timestamp)
                    gc.collect()
                    consulta_porLinhas()
        print('Tudo Concluído!')
        break        