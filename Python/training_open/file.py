#arquivo = open('notas.txt', 'w')

def read_file(name):
    arquivo = open('notas.txt', 'r')
    print(arquivo.read())

def write_file(name, text):
    arquivo = open(name, 'w')
    arquivo.write(text)

def att_file(name, text):
    arquivo = open(name, 'a')
    arquivo.write(text)

def media_alunos(name):
    arquivo = open('notas.txt')
    alunos_notas = arquivo.read()
    alunos_notas = alunos_notas.split('\n')
    alunos_notas.pop(0)
    media_notas = []
    
    for aluno_nota in alunos_notas:
        lista_alunos_notas = aluno_nota.split(',')
        aluno = lista_alunos_notas[0]
        lista_alunos_notas.pop(0)

        media = lambda notas: sum([int(i) for i in notas]) / len(notas)

        media_notas.append({aluno : media(lista_alunos_notas)})

    return media_notas
            

media = media_alunos('notas.txt')
write_file('media de notas.txt', 'Aluno >>>>>> Media')

for x in media:

    for y in x:
        att_file('media de notas.txt', f'\n{y} : {x[y]}')