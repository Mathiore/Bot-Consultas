import pyautogui as py
from PIL import Image
import time
import module
import gc
from datetime import datetime

#SEMPRE DEIXE O BLOCO DE NOTAS ABERTO E FIXO.

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
        linha = 0
        total_linhas = len(conteudo)
        while linha <= total_linhas:
            py.click(x=597, y=390)
            py.keyDown('ctrl')
            py.press('a')
            py.keyUp('ctrl')
            py.press('backspace')
            py.write(conteudo[linha])
            time.sleep(1)
            py.click(x=535, y=324)
            linha = linha + 1
            while 1:
                icon_pos = py.locateOnScreen('img/concluidosingle.png')
                bloqueio = py.locateOnScreen('img/bloqueiosingle.png')
                if icon_pos:
                    py.click(x=1046, y=596)
                    print('Consultado: ', conteudo[linha])
                    break
                elif bloqueio:
                    module.fechar_inova()
                    time.sleep(1800)
                    now = datetime.now()
                    timestamp = datetime.timestamp(now)
                    print('Já se passaram 30 minutos!')
                    print('Realizando Limpeza de memória!')
                    print("Horário agora: ", timestamp)
                    gc.collect()
                    consulta_porLinhas()



consulta_porLinhas()