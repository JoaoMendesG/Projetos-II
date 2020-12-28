import subprocess
import time
import pandas as pd
import numpy as np

print('Iniciando Programa !')
time.sleep(2)
print('Este programa tem por finalidade realizar uma varredura das redes locais wireless')
time.sleep(5)
print('na qual este dispositivo já se conectou,')
time.sleep(3)
print('retornando o nome da rede (wifi) e sua chave de acesso (senha).\n')
time.sleep(5)
print('Aguarde...\n')
time.sleep(5)

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('latin1').split('\n')

wifis = [line.split(':')[1][1:-1] for line in data if 'Todos os Perfis de Usu\xa0rios' in line]

#print(f'Data: {data}\nWIfis: {wifis}')
#time.sleep(10)

wifi_nomes = []
wifi_senhas = []

for wifi in wifis:
    resultado = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('latin1').split('\n')
    resultado = [line.split(':')[1][1:-1] for line in resultado if 'Conte£do da Chave' in line]
    
    wifi_nomes.append(wifi)

    if resultado == []:
        wifi_senhas.append('Não é possivel ser lido')
    else:
        wifi_senhas.append(resultado)
   
    try:
        print(f'Nome: {wifi}\nSenha: {resultado[0]}\n')
    except IndexError:
        print(f'Nome: {wifi}\nSenha: Não é possivel ser lido\n')

dict_pandas = {}
for contagem in range(len(wifi_senhas)):
    dict_pandas[wifi_nomes[contagem]] = wifi_senhas[contagem]

dataframe = pd.DataFrame(data= dict_pandas)
print('\nObrigado por escolher este serviço :) \n')
time.sleep(10)