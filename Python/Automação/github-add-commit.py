import shutil
import subprocess
import os

diretorio = input('\nInforme o caminho do projeto/diretório:\n>>>')

verificacao_diretorio = subprocess.getoutput(f'cd {diretorio}')
verificacao_principal = subprocess.getoutput(f'cd {diretorio} & git status')

if verificacao_principal == 'fatal: not a git repository (or any of the parent directories): .git' or verificacao_principal == "ls: cannot open directory '.': No such file or directory":
    print('\nRepositório inválido: não é um repositório git !')

elif verificacao_diretorio == 'O sistema não pode encontrar o caminho especificado.' or verificacao_diretorio == subprocess.getoutput('cd '):
    print('Diretório não existe !')

else:
    mensagens_git = ['On branch master', "Your branch is up to date with 'origin/master'.", '', 'nothing to commit, working tree clean']
    mensagens_git_dois = ['On branch master', 'nothing to commit, working tree clean']
    data = subprocess.getoutput(f'cd {diretorio} & git status').split('\n')
    verificacao = True

    if mensagens_git != data and mensagens_git_dois != data:
        print('\nTudo certo, iniciando versionamento...')

    else:
        print('\nÉ necessario que seja inserido um repositório com arquivos alterados e/ou criados !')
        verificacao = False

    if verificacao:
        mensagem_personalizada = input('\nGostaria de personalizar sua mensagem de commit ?(S/N)\n>>>').upper()
        mensagem_padrao = 'Update project.'

        if mensagem_personalizada == 'S' or mensagem_personalizada == 'SIM':
            mensagem_padrao = input('Digite a mensagem para commit: ')
        
        os.system(f'cd {diretorio} & git add * & git commit -m "{mensagem_padrao}"')
        data_check = subprocess.getoutput(f'cd {diretorio} & git status')
        print(data_check)

    else:
        print('\nReinicie o programa !')