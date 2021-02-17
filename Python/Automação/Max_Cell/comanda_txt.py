from time import sleep
from datetime import date, time, datetime

def criar_comanda(nome_do_funcionario):
    arquivo = open(f'funcionarios/{nome_do_funcionario}.txt', 'w')
    data_atual = datetime.now().strftime('%d/%m/%Y %H:%M')
    espaco = '-'*38
    print(arquivo.write(f'Nome: {nome_do_funcionario}\t\tData: {data_atual}\n{espaco}\nCodigo:\t\tQTD\t\tValor\t\t$|D|C|\n{espaco}'))

def lancamento_comanda(nome_do_funcionario):
    arquivo = open(f'funcionarios/{nome_do_funcionario}.txt', 'a')
    data_atual = datetime.now().strftime('%d/%m/%Y %H:%M')
    espaco = '-'*38
    arquivo.write(f'\n{espaco}\n{data_atual}\n{espaco}')

def escrever_comanda(funcionario, codigo_produto, qtd, valor_produto, forma_de_pagamento):
    try:
        arquivo = open(f'funcionarios/{funcionario}.txt', 'r')

    except FileNotFoundError:
        print('Nome de funcionário inválido.')
    
    except:
        print('Erro desconhecido')

    else:
        arquivo = open(f'funcionarios/{funcionario}.txt', 'a')

        if forma_de_pagamento == '$':
            pagamento = 'X| | |'
        elif forma_de_pagamento == 'D':
            pagamento = ' |X| |'
        elif forma_de_pagamento == 'C':
            pagamento = ' | |X|'

        if len(str(valor_produto)) >= 7:
            arquivo.write(f'\n{codigo_produto}\t\t\t{qtd}\t\t{valor_produto:.2f}\t{pagamento}')
        elif len(str(codigo_produto)) >= 4:
            arquivo.write(f'\n{codigo_produto}\t\t{qtd}\t\t{valor_produto:.2f}\t\t{pagamento}')
        else:
            arquivo.write(f'\n{codigo_produto}\t\t\t{qtd}\t\t{valor_produto:.2f}\t\t{pagamento}')

criar_comanda('Alan') #cadastra a comanda

escrever_comanda('Alan', 545, 1, 25.00, 'D') #inseri um registro na comanda
escrever_comanda('Alan', 54, 1, 15.00, '$')
escrever_comanda('Alan', 4542, 1, 24.00, 'C')
escrever_comanda('Alan', 54, 1, 11015.00, '$')

sleep(60) #aguarda 1 minuto, função da lib time

lancamento_comanda('Alan') #registra o horário de lançamento da comanda no sistema

escrever_comanda('Alan', 54, 1, 11015.00, 'CC') #erro pagamento invávildo
escrever_comanda('Eliana', 54, 1, 11015.00, '$') #erro comanda não cadastrada