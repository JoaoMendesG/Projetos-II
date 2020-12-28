# forma alternativa do arq ACME.INC.py

employees = {}
count = 0
confirmation = 'sim'.lower()
separator = '-'*60
run = 'sim'

print('Programa iniciado\nRegistre os seus funcionários com as seguintes informações:')

while confirmation == 'sim' or confirmation == 'si' or confirmation == 's':
    employee = str(input('\nNome do funcionário (primeiro nome): '))
    memory_used = float(input('Memória usada: '))

    if len(employee) < 13:
        while len(employee) < 13:
            employee += ' '
        
        count += 1
        employees[count] = [employee, memory_used]
    
    confirmation = input('Realizar outro registro ?: ').lower()

print(f'Total de funcionário registrados: {count}')

while run == 'si' or run == 'sim' or run == 's':

    menu = int(input('\nSelecione uma opção:\n\n1- Ordenado pela quantidade de memória usada.\n2- Visualizar uma certa quantidade de funcionários:\n3- Sem alteração:\n'))

    if menu == 3:
        total_memory = []

        # default print
        print(
            '\nACME Inc.\tUso do espaço em disco pelos usuários',
            '\n{}'.format(separator),
            '\n|N°\t|Usuário\t|Espaço utilizado(MB)\t|% do uso',
            '\n|\t|\t\t|\t\t\t|'
        )
        # to add values in the memory list
        for data in range(0, len(employees)):
            memorymb = employees[data + 1][1]/(1024*1024)

            total_memory.append(memorymb)
        
        # all the operation with the data of employees and the used memory
        for data in range(0, len(employees)):
            data_index = data + 1
            percent = total_memory[data] / sum(total_memory)

            print(
                '|{}\t|{}\t| {:.2f}   \t\t| {:.2f}'.format(data_index, employees[data_index][0], total_memory[data], percent)
            )

        # the final default print = total of memory used and the mean of memory
        print(
            '\nTotal de espaço ocupado: {:.2f} MB'.format(sum(total_memory)),
            '\nEspaço médio ocupado: {:.2f} MB'.format(sum(total_memory)/len(total_memory))
        )

    elif menu == 1:
        total_memory = []
        percentual = []

        # default print
        print(
            '\nACME Inc.\tUso do espaço em disco pelos usuários',
            '\n{}'.format(separator),
            '\n|N°\t|Usuário\t|Espaço utilizado(MB)\t|% do uso',
            '\n|\t|\t\t|\t\t\t|'
        )

        for data in range(0, len(employees)):
            memorymb = employees[data + 1][1]/(1024*1024)
            total_memory.append(memorymb)
        
        for data in range(0, len(employees)):
            percent = total_memory[data] / sum(total_memory)
            percentual.append(percent)

        percentual_sorted = sorted(percentual)

        for data in range(0, len(employees)):
            bigger = max(percentual_sorted)

            print(
                '|{}\t|{}\t| {:.2f}   \t\t| {:.2f}'.format(percentual.index(bigger)+1, 
                employees[percentual.index(bigger)+1][0], total_memory[percentual.index(bigger)], percentual[percentual.index(bigger)])
            )

            percentual_sorted.remove(bigger)

        # the final default print = total of memory used and the mean of memory
        print(
            '\nTotal de espaço ocupado: {:.2f} MB'.format(sum(total_memory)),
            '\nEspaço médio ocupado: {:.2f} MB'.format(sum(total_memory)/len(total_memory))
        )

    elif menu == 2:
        quant = int(input('Até quantos funcionários deseja viualizar ?: '))

        total_memory = []

        print(
            '\nACME Inc.\tUso do espaço em disco pelos usuários',
            '\n{}'.format(separator),
            '\n|N°\t|Usuário\t|Espaço utilizado(MB)\t|% do uso',
            '\n|\t|\t\t|\t\t\t|'
        )

        for data in range(0, len(employees)):
            memorymb = employees[data + 1][1]/(1024*1024)

            total_memory.append(memorymb)
        

        for data in range(0, quant):
            data_index = data + 1
            percent = total_memory[data] / sum(total_memory)

            print(
                '|{}\t|{}\t| {:.2f}   \t\t| {:.2f}'.format(data_index, employees[data_index][0], total_memory[data], percent)
            )

        print(
            '\nTotal de espaço ocupado (Todos os funcionários incluidos): {:.2f} MB'.format(sum(total_memory)),
            '\nEspaço médio ocupado (Todos os funcionários incluidos): {:.2f} MB'.format(sum(total_memory)/len(total_memory))
        )

    else:
        print('Entrada inválida...')

    run = str(input('\nDeseja retornar ao menu ?:'))

print('\nFinalizando...')