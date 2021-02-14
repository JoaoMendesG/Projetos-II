import shutil
import subprocess
import os

#diretorio = input('Informe o caminho do projeto:\n>>>')
nome_diretorio = input('Informe o nome do diretório:\n>>>')

os.mkdir(f'../../{nome_diretorio}')

pasta = open(f'../../{nome_diretorio}/README.md', 'w')
pasta.write('Criando um diretório git com um clique !')

os.system(f'cd ../../{nome_diretorio} & git init')