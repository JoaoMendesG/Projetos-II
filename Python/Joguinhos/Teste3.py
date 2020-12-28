# projeto de um jogo de adivinhação

import random
import time
valor = int(random.randint(1,100))
valor_sub = valor - 54
valor_soma = valor + 123
valor_mult = valor * 9
s = input('Olá, está pronto para o jogo de cálculo ?').lower()
if s == 'sim' or s == 's' or s == 'si':
    print('Lets bora !!!')
else:
    print('Ok, tchau !!')
    time.sleep(2)
    print('Brincadeira !')
    time.sleep(1)
    print('Responda !:')
time.sleep(2)
print('Um número menos 54 é igual à: {}'.format(valor_sub))
print('O mesmo número mais 123 é igual à: {}'.format(valor_soma))
print('O mesmo número multiplicado por 9 é igual à: {}'.format(valor_mult))
time.sleep(5)
resu = int(input('Qual é esse número ?: '))
if resu == valor:
    print('Acerto mizerávi !')
else:
    print('Achou que era {} !'.format(resu))
    time.sleep(2)
    print('Achou errado otário !!!')
time.sleep(1)
print('Era {} !'.format(valor))
time.sleep(3)