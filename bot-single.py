import pyautogui as py
from PIL import Image
import time
import module
import gc
from datetime import datetime


py.alert(text='Digite o acesso da conta: ', title='Alerta', button='OK')
usuario = input('Digite o usuário: ')
senha = input('Digite a senha: ')
py.alert(text='Digite o período da Consulta!', title='Alerta', button='OK')
dia_inicial = input('Digite o dia inicial da consulta: ')
mes_inicial = input('Digite o mês inicial da consulta: ')
dia_final = input('Digite o dia final da consulta: ')
mes_final = input('Digite o mês final da consulta: ') 

def consulta_1v1():

    while 1:
        module.verifica_inova(usuario, senha)

        module.verificatela_di()

        #Clica na aba de Di's
        py.click(x=586, y=313) 
        module.datas_single(dia_inicial, mes_inicial, dia_final, mes_final)

        time.sleep(3)
        
        while 1:
            retifica_btn = py.locateOnScreen('img/botao_retificacao.png')
            if retifica_btn:
                py.click(retifica_btn)
                break


        position_x = 1132 
        position_y = 525
        consult_x = 1144
        consult_y = 530
        i = 0
        n = 10

        while i < n:
            py.click(x=position_x, y=position_y)
            py.click(button='right')
            py.click(x=consult_x, y=consult_y)
            time.sleep(1)
            py.click(x=1177, y=650)
            time.sleep(5)
            bloqueio_receita = py.locateOnScreen('img/bloqueiocomex.png')
            if bloqueio_receita:
                py.click(x=1396, y=289)
                module.fechar_inova()
                time.sleep(120)
                consulta_1v1()
            else:
                py.click(x=535, y=324)
            while 1:
                icon_pos = py.locateOnScreen('img/concluidosingle.png')
                retificado = py.locateOnScreen('img/retificado.png')
                bloqueio = py.locateOnScreen('img/bloqueiosingle.png')
                if bloqueio:
                    module.copiar_di()
                    py.click(x=658, y=1063)
                    py.click(x=1398, y=287)
                    module.fechar_inova()
                    time.sleep(1800)
                    now = datetime.now()
                    timestamp = datetime.timestamp(now)
                    print('Já se passaram 30 minutos!')
                    print('Realizando Limpeza de memória!')
                    print("Horário agora: ", timestamp)
                    gc.collect()
                    consulta_1v1()
                elif icon_pos:
                    py.click(x=1046, y=596)
                    py.click(x=1403, y=289)
                    break
                elif retificado:
                    print('Consultas já Finalizadas')
                    break
            #position_x = position_x+2
            #position_y = position_y+20
            #consult_x = consult_x+5
            #consult_y = consult_y+30
            py.click(x=position_x, y=position_y)
            py.click(x=386, y=340)
            time.sleep(10)
            py.click(1123, 491)
            retificado = py.locateOnScreen('img/retificado.png')
            if retificado:
                print('Consultas Finalizadas')
                break

consulta_1v1()

module.consulta_porLinhas(usuario, senha, dia_inicial, mes_inicial, dia_final, mes_final)