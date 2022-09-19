import pyautogui as py
from PIL import Image
import time
import module
import gc
from datetime import datetime

#SEMPRE DEIXE O BLOCO DE NOTAS ABERTO E FIXO.

linha = 0

def consulta_porLinhas():
    while 1:
        di_perdidas = open('dis_perdidas.txt', 'r')
        conteudo = di_perdidas.readlines()
        module.verifica_inova()

        module.verificatela_di()

        #Clica na aba de Di's
        py.click(x=586, y=313)

        module.datas_single()
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
                module.fechar_inova()
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
                if icon_pos:
                    py.click(x=1046, y=596)
                    print('Concluido!')
                    break
                elif bloqueio:
                    print('Falhou!')
                    print('Apagando DIs Concluídas.')
                    i = 0
                    py.click(x=715, y=1060)
                    py.click(x=380, y=325)
                    while i < linha:
                        py.keyDown('ctrl')
                        py.keyDown('alt')
                        py.press()
                    py.click(x=1394, y=285)
                    module.fechar_inova()
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


consulta_porLinhas()