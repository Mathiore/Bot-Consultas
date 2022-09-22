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
        while 1:
            aba_consulta = py.locateOnScreen('img/aba_consulta.png', confidence=0.9)
            if aba_consulta:
                py.click(aba_consulta)
                break

        module.datas_single(dia_inicial, mes_inicial, dia_final, mes_final)

        time.sleep(3)
        
        while 1:
            retifica_btn = py.locateOnScreen('img/botao_retificacao.png', confidence= 0.9)
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
            retificado = py.locateOnScreen('img/retificado.png')
            if retificado:
                print('Consultas Finalizadas Já!')
                break

            py.click(x=position_x, y=position_y)
            py.click(button='right')
            py.click(x=consult_x, y=consult_y)
            time.sleep(1)
            py.click(x=1177, y=650)
            time.sleep(5)
            bloqueio_receita = py.locateOnScreen('img/bloqueiocomex.png', confidence= 0.9)
            if bloqueio_receita:
                py.click(x=1396, y=289)
                module.fechar_inova()
                time.sleep(120)
                consulta_1v1()
            else:
                py.click(x=535, y=324)
            while 1:
                icon_pos = py.locateOnScreen('img/concluidosingle.png', confidence= 0.9)
                retificado = py.locateOnScreen('img/retificado.png')
                bloqueio = py.locateOnScreen('img/bloqueiosingle.png', confidence= 0.9)
                inova_icon = py.locateOnScreen('img/inova_icon.png', confidence= 0.9)
                siscomex_error = py.locateOnScreen('img/erro_server.png', confidence=0.9)
                if bloqueio:
                    module.copiar_di()
                    py.click(inova_icon)
                    py.click(x=1398, y=287)
                    module.fechar_inova()
                    print("Horário agora: ", datetime.today())
                    time.sleep(1800)
                    print('Já se passaram 30 minutos!')
                    print('Realizando Limpeza de memória!')
                    gc.collect()
                    consulta_1v1()
                elif icon_pos:
                    py.click(x=1046, y=596)
                    py.click(x=1403, y=289)
                    break
                elif retificado:
                    print('Consultas já Finalizadas')
                    break
                elif siscomex_error:
                    print('Siscomex fora de Ar.')
                    module.copiar_di()
                    py.click(inova_icon)
                    py.click(x=1398, y=287)
                    module.fechar_inova()
                    time.sleep(600)
                    gc.collect()
                    consulta_1v1()
            
            py.click(x=position_x, y=position_y)
            #CLICA EM BOTÃO DE EXIBIR DI's
            #py.click(x=386, y=340)
            if position_y <= 720:
                position_y = position_y+20
                consult_y = consult_y+20
            time.sleep(5)
            py.press('down')

        retificado = py.locateOnScreen('img/retificado.png')
        sair_di = py.locateOnScreen('img/exit_di.png', confidence= 0.9)
        if retificado:
            print('Consultas Finalizadas')
            py.click(sair_di)
            break
py.click(x=1144, y=288)
consulta_1v1()
print('Finalizado Consulta Geral!')
py.click(x=1144, y=288)
module.consulta_porLinhas(usuario, senha, dia_inicial, mes_inicial, dia_final, mes_final)